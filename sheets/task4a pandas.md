# T Level DSD -- Task 4A Cheat Sheet

## Exploratory Data Analysis (EDA) with Python and Pandas

A quick-reference guide to the main ideas and code snippets for
exploring a dataset.

------------------------------------------------------------------------

## 1. What is EDA?

**Exploratory Data Analysis (EDA)** is the process of examining a
dataset to understand its structure, spot missing or unusual data, find
patterns, and prepare it for analysis.

Key terms:

-   **Dataset:** a collection of data.
-   **DataFrame:** a table of data with rows and columns.
-   **Series:** one column of a DataFrame.
-   **Row:** one record or observation.
-   **Column:** one feature or variable.
-   **CSV:** a comma-separated values file.
-   **Missing value:** data that is blank or unavailable.

## 2. Import libraries and load data

``` python
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
```

-   `pandas` is commonly shortened to `pd`.
-   `numpy` is commonly shortened to `np`.
-   `df` is a common variable name for a DataFrame.

## 3. Inspect the dataset

``` python
df.head()       # First 5 rows
df.tail()       # Last 5 rows
df.sample(5)    # 5 random rows
df.shape        # (number of rows, number of columns)
df.columns      # Column names
df.index        # Row index
df.info()       # Column names, data types and non-null counts
df.dtypes       # Data type of each column
df.describe()   # Summary statistics for numeric columns
```

**Example:** if `df.shape` returns `(3333, 20)`, the dataset has 3,333
rows and 20 columns.

## 4. Data types

  Data type   Meaning                  Example
  ----------- ------------------------ ------------
  `int64`     Whole number             `25`
  `float64`   Decimal number           `25.5`
  `object`    Often text/string data   `"London"`
  `bool`      True or False            `True`

Convert a column's data type:

``` python
df["Churn"] = df["Churn"].astype("int64")
```

Only convert a column when the values are suitable for the target type.

## 5. Summary statistics

``` python
df.describe()
df["Age"].mean()       # Average
df["Age"].median()     # Middle value
df["Age"].mode()       # Most common value
df["Age"].min()        # Smallest value
df["Age"].max()        # Largest value
df["Age"].std()        # Standard deviation (spread)
df["Age"].count()      # Number of non-missing values
```

  Statistic   Meaning
  ----------- -----------------------------------------------
  `count`     Number of non-missing values
  `mean`      Average
  `std`       Standard deviation; how spread out values are
  `min`       Smallest value
  `25%`       Lower quartile
  `50%`       Median
  `75%`       Upper quartile
  `max`       Largest value
  Range       Maximum minus minimum

## 6. Count and inspect categories

``` python
df["Churn"].value_counts()                    # Count each value
df["Churn"].value_counts(normalize=True)       # Proportions
df["State"].unique()                           # List unique values
df["State"].nunique()                          # Number of unique values
```

Use `value_counts()` to see how frequently each category occurs.

## 7. Sorting data

``` python
df.sort_values(by="Age")  # Smallest to largest

df.sort_values(
    by="Age",
    ascending=False
)  # Largest to smallest

df.sort_values(
    by=["Age", "Salary"],
    ascending=[True, False]
)  # Sort by multiple columns
```

-   `ascending=True`: smallest to largest (A to Z).
-   `ascending=False`: largest to smallest (Z to A).

## 8. Selecting columns and filtering rows

``` python
df["Age"]                    # Select one column
df[["Age", "Salary"]]        # Select multiple columns

df[df["Age"] > 18]           # Rows where Age is over 18
df[df["Age"] == 18]          # Rows where Age equals 18
df[df["Age"] != 18]          # Rows where Age is not 18

# Two conditions: AND
df[(df["Age"] > 18) & (df["Salary"] > 20000)]

# Two conditions: OR
df[(df["Age"] < 18) | (df["Salary"] > 50000)]
```

Comparison operators:

  Operator   Meaning
  ---------- --------------------------
  `==`       Equal to
  `!=`       Not equal to
  `>`        Greater than
  `<`        Less than
  `>=`       Greater than or equal to
  `<=`       Less than or equal to
  `&`        AND (both conditions)
  `\|`       OR (either condition)

Put each condition in brackets when combining conditions with `&` or
`|`.

## 9. `loc` vs `iloc`

``` python
df.loc[0:5, ["State", "Age"]]  # Select using row/column labels
df.iloc[0:5, 0:3]              # Select using integer positions
```

-   **`loc` = labels.**
-   **`iloc` = integer positions.**
-   With `iloc`, the ending position is excluded. With label slicing in
    `loc`, the ending label is normally included.

## 10. Missing data

``` python
df.isna().sum()                 # Missing values in each column
df.isna().sum().sum()           # Total missing values
df.dropna()                     # Return rows with missing values removed
df["Age"].fillna(df["Age"].mean())  # Fill missing Age values with the mean
```

Check missing data before deciding whether to remove or replace it. Do
not automatically delete missing values: consider what they mean and how
much data would be lost.

## 11. Applying functions and changing values

``` python
df.apply(np.max)                # Maximum of each applicable column
df["Age"].apply(lambda x: x * 2)  # Apply a function to each Age value
```

A `lambda` is a short, anonymous function. Here, `lambda x: x * 2`
doubles `x`.

Use `map()` to map values in a Series:

``` python
mapping = {"Yes": True, "No": False}
df["Plan"] = df["Plan"].map(mapping)
```

Use `replace()` to replace matching values:

``` python
df["Plan"] = df["Plan"].replace({"Yes": True, "No": False})
```

**Difference:** values not listed in a `map()` dictionary become missing
(`NaN`). `replace()` leaves unmatched values unchanged.

## 12. Grouping data

``` python
df.groupby("Churn")["Age"].mean()  # Average age in each Churn group
df.groupby("Churn")["Age"].max()   # Maximum age in each group
df.groupby("Churn")["Age"].min()   # Minimum age in each group
df.groupby("Churn")["Age"].sum()   # Total age in each group

df.groupby("Churn")["Age"].agg(["mean", "min", "max"])
```

`groupby()` puts rows with the same category together so you can
calculate statistics for each group.

## 13. Crosstabs and pivot tables

``` python
pd.crosstab(df["Churn"], df["Plan"])
```

A **crosstab** counts combinations of categories.

``` python
df.pivot_table(
    values="Salary",
    index="Department",
    aggfunc="mean"
)
```

A **pivot table** summarises values using an aggregation such as `mean`,
`sum` or `count`.

## 14. Creating and deleting columns or rows

``` python
# Create a new column
df["Total"] = df["Maths"] + df["English"]

# Insert a new column at a chosen position
df.insert(0, "DoubleAge", df["Age"] * 2)

# Drop a column (axis=1)
df = df.drop("Age", axis=1)

# Drop a row by index label (axis=0)
df = df.drop(0, axis=0)
```

-   `axis=0`: rows.
-   `axis=1`: columns.
-   Assigning the result back to `df` keeps the change.

## 15. Visualising data

``` python
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x="Churn", data=df)
plt.show()
```

Common charts:

  ---------------------------------------------------------------------
  Chart                              Useful for
  ---------------------------------- ----------------------------------
  Bar chart                          Comparing categories

  Histogram                          Showing the distribution of
                                     numerical data

  Line graph                         Showing change over time

  Scatter plot                       Exploring the relationship between
                                     two numerical variables

  Box plot                           Showing median, spread and
                                     possible outliers
  ---------------------------------------------------------------------

## 16. Telecom churn example

**Churn** means a customer stops using a company's service.

The Kaggle tutorial uses a telecom customer dataset to explore which
customer characteristics may be associated with leaving.

Example questions EDA can help investigate:

-   How many customers left?
-   What proportion of customers left?
-   Is churn different for customers with an international plan?
-   Do customers who contact customer service more often have different
    churn rates?

Example code:

``` python
df["Churn"].value_counts()
df["Churn"].value_counts(normalize=True)

pd.crosstab(df["Churn"], df["International plan"], normalize="columns")

df.groupby("Churn")["Customer service calls"].mean()
```

Use the results to identify patterns. A pattern or association does
**not** automatically prove that one factor causes another.

## 17. Quick command reference

  Task                  Command
  --------------------- -----------------------------
  Read a CSV            `pd.read_csv("data.csv")`
  First rows            `df.head()`
  Last rows             `df.tail()`
  Dimensions            `df.shape`
  Column names          `df.columns`
  Data overview         `df.info()`
  Summary statistics    `df.describe()`
  Count categories      `df["col"].value_counts()`
  Unique values         `df["col"].unique()`
  Sort                  `df.sort_values("col")`
  Filter                `df[df["col"] > 10]`
  Select by labels      `df.loc[...]`
  Select by positions   `df.iloc[...]`
  Missing values        `df.isna().sum()`
  Group rows            `df.groupby("col")`
  Cross-tabulation      `pd.crosstab(...)`
  Pivot table           `df.pivot_table(...)`
  Change type           `df["col"].astype("int64")`
  Replace values        `df["col"].replace({...})`
  Apply a function      `df["col"].apply(...)`
  Remove rows/columns   `df.drop(...)`

## 18. Test-yourself reminders

1.  **EDA** = Exploratory Data Analysis.
2.  **DataFrame** = a table; **Series** = one column.
3.  `head()` = first rows; `tail()` = last rows.
4.  `shape` = rows and columns.
5.  `info()` = structure and data types.
6.  `describe()` = numerical summary statistics.
7.  `mean` = average; `median` = middle; `mode` = most common.
8.  `loc` = labels; `iloc` = integer positions.
9.  `groupby()` = group matching values for analysis.
10. `value_counts()` = count how often each value appears.
11. `axis=0` = rows; `axis=1` = columns.
12. **Churn** = customers leaving a service.

------------------------------------------------------------------------

## Revision priority

If you are short on time, practise these first:

-   Loading a CSV with `pd.read_csv()`.
-   Inspecting data with `head()`, `shape`, `info()` and `describe()`.
-   Selecting and filtering rows.
-   Understanding `loc` and `iloc`.
-   Counting and grouping with `value_counts()` and `groupby()`.
-   Explaining what your results show in plain English.

**Remember:** understand what each command does and when you would use
it. Do not just memorise the code.

------------------------------------------------------------------------

## 19. More filtering techniques

### `isin()` --- match several possible values

``` python
# Keep rows where the State is either London, Essex or Kent
df[df["State"].isin(["London", "Essex", "Kent"])]
```

### `between()` --- filter within a range

``` python
# Keep rows where Age is between 18 and 30 (inclusive)
df[df["Age"].between(18, 30)]
```

### `contains()` --- find text containing a word

``` python
# Find rows where the Runner name contains "Smith"
df[df["Runner"].str.contains("Smith", case=False, na=False)]
```

-   `case=False` makes the search ignore capitalisation.
-   `na=False` treats missing text as not matching.

### Combine filtering techniques

``` python
# Age between 18 and 30 AND State is London or Essex
df[
    df["Age"].between(18, 30)
    & df["State"].isin(["London", "Essex"])
]
```

Remember to put each condition in brackets when using `&` or `|`.

## 20. Working with dates

Convert a column into a proper date type:

``` python
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d/%m/%Y",
    errors="coerce"
)
```

-   `dayfirst` / `format` helps Pandas interpret dates correctly.
-   `errors="coerce"` turns invalid dates into `NaT` (a missing date).

Extract parts of a date:

``` python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
```

Filter by a date range:

``` python
start_date = "2025-01-01"
end_date = "2025-12-31"

date_results = df[
    df["Date"].between(start_date, end_date)
]
```

Filter for one particular year:

``` python
df[df["Date"].dt.year == 2025]
```

**Important:** convert the column using `pd.to_datetime()` before using
`.dt`.

## 21. More sorting and grouping examples

Sort by date, newest first:

``` python
df.sort_values(by="Date", ascending=False)
```

Sort by prize money, highest first:

``` python
df.sort_values(by="Prize Money", ascending=False)
```

Group by a category and calculate totals:

``` python
df.groupby("Runner")["Prize Money"].sum()
```

Group by year and calculate average prize money:

``` python
df.groupby(df["Date"].dt.year)["Prize Money"].mean()
```

Group by more than one column:

``` python
df.groupby(["Runner", "Position"])["Prize Money"].sum()
```

Use `.agg()` to calculate several statistics at once:

``` python
df.groupby("Runner")["Prize Money"].agg(
    ["count", "sum", "mean", "max"]
)
```

-   `count` = number of values.
-   `sum` = total.
-   `mean` = average.
-   `max` = largest value.

## 22. Exception handling

Exception handling stops common errors from crashing the program
unexpectedly.

### Common exceptions

  -----------------------------------------------------------------------
  Exception                           What it usually means
  ----------------------------------- -----------------------------------
  `FileNotFoundError`                 The file does not exist at the
                                      specified location

  `ValueError`                        A value is the wrong format, such
                                      as text instead of a number

  `KeyError`                          A dictionary key or DataFrame
                                      column does not exist

  `TypeError`                         An operation is being used with an
                                      unsuitable type

  `ZeroDivisionError`                 The program tried to divide by zero

  `pd.errors.EmptyDataError`          The CSV file is empty

  `pd.errors.ParserError`             Pandas could not parse the CSV
                                      correctly
  -----------------------------------------------------------------------

### Validate a number entered by the user

``` python
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")
```

### Handle a missing column

``` python
try:
    average = df["Age"].mean()
except KeyError:
    print("The Age column is missing.")
```

### Handle division by zero

``` python
if len(results) > 0:
    average = results["Prize Money"].sum() / len(results)
else:
    print("There are no results to calculate.")
```

**Good practice:** - Catch specific exceptions rather than using a bare
`except:`. - Give the user a clear, helpful error message. - Do not
display technical tracebacks to ordinary users. - Never use `eval()` to
process user input.

## 23. Testing your program

Test more than just the normal situation. Check what happens when the
user makes mistakes or the data is unusual.

  -----------------------------------------------------------------------
  Test                    Example                 Expected result
  ----------------------- ----------------------- -----------------------
  Valid input             User enters menu option Correct report opens
                          `1`                     

  Invalid menu input      User enters `hello`     Friendly error; menu
                                                  appears again

  Out-of-range choice     User enters `99`        Choice is rejected

  Missing CSV             Rename or move the CSV  Friendly file-not-found
                                                  message

  Empty CSV               Use an empty file       Program handles it
                                                  without crashing

  No matching results     Search for an unknown   "No results found"
                          runner                  message

  Invalid date            Enter an impossible     Date is rejected or
                          date                    handled safely

  Missing values          Include blank cells     Missing values are
                                                  handled

  Duplicate rows          Include repeated        Duplicates are
                          records                 identified or removed
                                                  if appropriate

  Exit option             User chooses Exit       Program closes cleanly
  -----------------------------------------------------------------------

### A simple testing checklist

-   [ ] Does the program load the correct CSV?
-   [ ] Does it handle a missing or empty file?
-   [ ] Does every menu option work?
-   [ ] Does invalid input get rejected?
-   [ ] Does filtering return the correct rows?
-   [ ] Are calculations correct?
-   [ ] Does it handle no matching results?
-   [ ] Are reports easy to read?
-   [ ] Do graphs have titles and labelled axes?
-   [ ] Does the program exit properly?

**Testing tip:** record the test input, expected result, actual result
and whether it passed. Fix problems and test again.

------------------------------------------------------------------------

## 24. Quick Task 4A program structure

A typical menu-driven program can follow this pattern:

``` python
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "results.csv"


def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("The data file could not be found.")
        return None


def show_menu():
    print("\\n1. Show results")
    print("2. Show summary")
    print("3. Exit")


def main():
    df = load_data(DATA_FILE)

    if df is None:
        return

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(df.head())
        elif choice == "2":
            print(df.describe())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
```

This is a **basic pattern**, not a complete answer for every assessment
brief. Adapt the functions, columns, menu choices and calculations to
the actual task.

## 25. Task 4A assessment priorities

When developing your program, remember that it needs to do more than
run.

-   **Organisation:** use functions, meaningful names, constants and
    clear structure.
-   **User experience:** provide clear menus, useful messages and
    readable reports.
-   **Functionality:** make sure the required features work correctly.
-   **Security:** validate input, avoid `eval()` and handle errors
    safely.
-   **Logic:** use correct conditions, calculations and filtering.
-   **Robustness:** handle missing files, invalid data and empty
    results.

The exact requirements and marks depend on the assessment brief. Use the
brief as your checklist.

------------------------------------------------------------------------

## Final revision priorities

If you are short on time, practise these first:

1.  Loading a CSV with `pd.read_csv()`.
2.  Inspecting data with `head()`, `shape`, `info()` and `describe()`.
3.  Selecting and filtering rows with conditions, `isin()` and
    `between()`.
4.  Converting and filtering dates with `pd.to_datetime()` and `.dt`.
5.  Grouping and sorting with `groupby()` and `sort_values()`.
6.  Handling invalid input with `try` / `except`.
7.  Testing valid, invalid, missing-file and no-results situations.
8.  Explaining what your results show in plain English.

**Remember:** understand what each command does, when to use it, and how
it helps your program meet the assessment brief.
