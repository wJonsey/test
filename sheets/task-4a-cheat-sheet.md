# Task 4a · Coding with pandas

**34 marks** · Organisation 8 · User experience 8 · Functionality 6 · Security 6 · Logic 3 · Robustness 3

> **The big idea:** half the marks are for *how neat and friendly* the program is, not just whether it runs.

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### What is pandas?

**pandas** is a Python library for working with tables of data. A pandas table is called a **DataFrame**:

- rows are individual records, such as one race;
- columns are fields, such as `Runner`, `Date`, `Position` and `Prize Money`;
- pandas provides tools to load, clean, filter and summarise the table.

The basic program journey is:

**Load the CSV → check the data → ask the user → filter rows → calculate → display a report or graph**

Think of the program as six simple jobs. Finish one job before moving to the
next. The examples below show the important pattern rather than a complete
program.

---

## 1. Organise the program

Put each job in its own function:

| Job | Example function | What it does |
|-----|------------------|--------------|
| Load | `load_data()` | Opens and cleans the CSV |
| Ask | `get_menu_choice()` | Gets a valid answer |
| Filter | `filter_results()` | Keeps matching rows |
| Calculate | `get_position_counts()` | Produces numbers or totals |
| Show | `show_prize_money()` | Prints a report |
| Graph | `plot_positions()` | Displays a labelled chart |

Use a small function for each responsibility. This avoids copied code and
long, deeply nested blocks.

```python
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "results.csv"
OPTIONS = ("Positions", "Prize money", "Graph", "Exit")


def main():
    """Load data and run the menu until the user chooses Exit."""
    data = load_data(DATA_FILE)
    if data is None:
        return

    while True:
        choice = get_menu_choice(OPTIONS)
        if choice == len(OPTIONS):
            print("Goodbye.")
            return
        if choice == 1:
            show_positions(data)
        elif choice == 2:
            show_prize_money(data)
        elif choice == 3:
            plot_positions(data)


if __name__ == "__main__":
    main()
```

Read the `main()` function from top to bottom: it loads the data, shows the
menu, calls the selected function, and repeats until **Exit**.

`print()` shows something to the user. `return` sends a value back to the part of the program that called the function. Processing functions should usually `return`; report functions should usually `print`.

---

## 2. Load safely

`read_csv()` loads the file. The cleaning lines convert the date and money columns into useful types. `errors="coerce"` changes an invalid value into a missing value so you can handle it safely.

```python
def load_data(filename):
    """Load and clean the CSV."""
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Can't find {filename}.")
        return None
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:
        print(f"Could not read the file: {error}")
        return None

    required_columns = {"Date", "Runner", "Position", "Prize Money"}
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        print(f"Missing required columns: {missing}.")
        return None

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df["Prize Money"] = pd.to_numeric(df["Prize Money"], errors="coerce").fillna(0)
    return df.dropna(subset=["Date", "Runner"])
```

After loading, inspect the table while developing. These commands help you
spot a wrong column name, an unexpected data type, or missing values:

```python
print(df.head())       # first five rows
print(df.shape)        # rows and columns
print(df.columns)      # available column names
df.info()              # data types and non-null counts
print(df.describe())   # numeric summary
```

Do not leave temporary inspection `print()` statements in the final product.

---

## 3. Validate every input

Do not trust what the user types. Keep asking until the answer is valid.

```python
def get_menu_choice(options):
    while True:
        answer = input("Choice: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print(f"Please enter a number from 1 to {len(options)}.")
```

> ⚠️ Never use unchecked input as a list index. `list[0 - 1]` is `list[-1]`, the **wrong item**.

---

## 4. Filter rows

Filtering means keeping only the rows that match the user's choices. A **mask** is a column of `True` and `False` values; `.loc[mask]` keeps the `True` rows. `.copy()` creates a safe separate result.

```python
# Keep the rows for one person in one date range.
mask = (df["Runner"] == name) & df["Date"].between(start, end)
results = df.loc[mask].copy()
```

The `&` means **and**. Each condition must be in brackets. The result is a
new DataFrame, so later changes do not accidentally change the original data.

## 5. Calculate useful results

```python
# Count each position, including positions that do not appear.
ORDER = ["1st", "2nd", "3rd", "Top 10", "Finished"]
counts = results["Position"].value_counts().reindex(ORDER, fill_value=0)

# Check for and remove common data problems.
print(df.isna().sum())       # missing values per column
df = df.drop_duplicates()    # remove repeated rows
print(df["Position"].unique()) # distinct position values
```

`value_counts()` counts categories. `reindex(..., fill_value=0)` adds a zero
when a category is missing. `sum()` adds values and `mean()` calculates the
average.

```python
total = results["Prize Money"].sum()
average = results["Prize Money"].mean()
```

---

## 6. Organise code for the brief

Avoid several pages of copied procedural code and deeply nested `if`/`for`
blocks. Use:

```python
DATA_FILE = "results.csv"       # constant
OPTIONS = ("Positions", "Prize money", "Graph", "Exit")


def calculate_total(results):
    """Return a value without printing or changing global state."""
    return results["Prize Money"].sum()
```

- Keep variables local where possible.
- Use constants for filenames, menu options, and fixed categories.
- Give each function one purpose and a docstring.
- Use pre-written libraries and your own modules through clear interfaces.
- Keep formatting and naming consistent.
- Add comments only where they explain non-obvious logic.

---

## 7. Make output friendly

| Need | Code | Shows |
|------|------|-------|
| Money | `f"£{1550.5:,.2f}"` | £1,550.50 |
| Percent | `f"{66.666:.1f}%"` | 66.7% |
| Columns | `f"{'Gold':<8}{3:>3}"` | `Gold      3` |

```python
if results.empty:
    print("No results found for that person and date range.")
    return
```

**Graphs:** title, x label, y label, `plt.tight_layout()`, then `plt.show()`.

```python
counts = results["Position"].value_counts()
counts.plot(kind="bar")
plt.title("Positions by event")
plt.xlabel("Position")
plt.ylabel("Races")
plt.tight_layout()
plt.show()
```

---

## 8. Defensive programming and security

Defensive programming anticipates bad input, missing data, and unexpected
states:

```python
if results.empty:
    print("No matching results were found.")
    return

try:
    value = float(input("Enter a value: "))
except ValueError:
    print("Please enter a number.")
```

Handle missing files, empty files, malformed CSVs, invalid dates, missing
columns, and empty filtered results. Do not expose tracebacks or sensitive
data. Never use `eval()` on input, and do not use broad `except:` blocks.

---

## 9. Always / never

| ✅ Always | ❌ Never |
|----------|---------|
| Validate all input | `eval()` on input |
| Use specific exceptions | Bare `except:` |
| Show a friendly message | Show a traceback |
| Use `.copy()` after filtering | Change the original data |
| Docstring on every function | Leave debug `print`s |
| Constants and local variables | Unnecessary mutable globals |
| Clear module/function interfaces | Copy-pasted nested code |
| Defensive checks and specific errors | Trust malformed data |

---

## Final check

- [ ] `main()` + `if __name__ == "__main__":`
- [ ] Input, process, output separated
- [ ] Functions/modules have clear interfaces
- [ ] Constants used and globals kept minimal
- [ ] Menu repeats until Exit
- [ ] CSV errors handled
- [ ] Dates and menu choices validated
- [ ] Data inspected with `.head()` and `.info()`
- [ ] "No results" message
- [ ] Money, tables and graphs formatted
- [ ] Graphs show meaningful trends or patterns with labels/legend where needed
- [ ] Product is consistent and simplifies user input
- [ ] Exceptions and malformed data handled defensively
- [ ] Missing values and duplicate rows considered
- [ ] Testing is evident through a working product meeting the brief
- [ ] No debug output
