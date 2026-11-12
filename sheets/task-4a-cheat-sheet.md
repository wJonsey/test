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
- columns are fields, such as `Runner`, `Date` and `Prize Money`;
- pandas provides tools to load, clean, filter and summarise the table.

The basic program journey is:

**Load the CSV → check the data → ask the user → filter rows → calculate → display a report or graph**

--


```

`main()` loads the data, then loops on the menu until **Exit**.

```python
if __name__ == "__main__":
    main()
```

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

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df["Prize Money"] = pd.to_numeric(df["Prize Money"], errors="coerce").fillna(0)
    return df.dropna(subset=["Date", "Runner"])
```

Check the data before processing it:

```python
print(df.head())       # first five rows
print(df.shape)        # rows and columns
print(df.columns)      # available column names
df.info()              # data types and non-null counts
print(df.describe())   # numeric summary
```

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

## 4. Filter, count, total

Filtering means keeping only the rows that match the user's choices. A **mask** is a column of `True` and `False` values; `.loc[mask]` keeps the `True` rows. `.copy()` creates a safe separate result.

```python
# One mask, then copy
mask = (df["Runner"] == name) & df["Date"].between(start, end)
results = df.loc[mask].copy()

# Missing categories show 0, not None
ORDER = ["1st", "2nd", "3rd", "Top 10", "Finished"]
counts = results["Position"].value_counts().reindex(ORDER, fill_value=0)

# Totals
results["Prize Money"].sum()
results["Prize Money"].mean()
results.groupby("Event")["Prize Money"].agg(["count", "sum", "mean"])

# Cleaning helpers
print(df.isna().sum())       # missing values per column
df = df.drop_duplicates()    # remove repeated rows
df["Position"].unique()      # distinct position values
```

---

## 5. Make output friendly

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

## 6. Always / never

| ✅ Always | ❌ Never |
|----------|---------|
| Validate all input | `eval()` on input |
| Use specific exceptions | Bare `except:` |
| Show a friendly message | Show a traceback |
| Use `.copy()` after filtering | Change the original data |
| Docstring on every function | Leave debug `print`s |

---

## Final check

- [ ] `main()` + `if __name__ == "__main__":`
- [ ] Input, process, output separated
- [ ] Menu repeats until Exit
- [ ] CSV errors handled
- [ ] Dates and menu choices validated
- [ ] Data inspected with `.head()` and `.info()`
- [ ] "No results" message
- [ ] Money, tables and graphs formatted
- [ ] Missing values and duplicate rows considered
- [ ] No debug output
