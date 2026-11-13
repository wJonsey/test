# T Level DSD – Task 4A Matplotlib Cheat Sheet

A practical revision guide to the Matplotlib skills you are most likely to need when analysing data and presenting results in Task 4A.

> **Important:** This is a focused Task 4A guide, not documentation for every feature in the entire Matplotlib library. It covers the common plotting commands, chart types, labels, formatting, saving and troubleshooting that are useful for data analysis.

---

## 1. What is Matplotlib?

**Matplotlib** is a Python library used to create graphs and charts from data.

The most common part is `matplotlib.pyplot`, normally shortened to `plt`.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
```

- `pandas` (`pd`) loads and works with tabular data.
- `matplotlib.pyplot` (`plt`) creates charts.
- `df` is a common name for a DataFrame.

---

## 2. The basic graph structure

Most simple charts follow this pattern:

```python
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("My Graph")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.show()
```

| Command | What it does |
|---|---|
| `plt.figure()` | Creates a new figure (the overall chart area) |
| `figsize=(8, 5)` | Sets width and height in inches |
| `plt.plot(x, y)` | Draws a line graph |
| `plt.title()` | Adds a chart title |
| `plt.xlabel()` | Labels the horizontal axis |
| `plt.ylabel()` | Labels the vertical axis |
| `plt.show()` | Displays the chart |

**Remember:** put `plt.show()` at the end of a chart so it is displayed.

---

## 3. Line graph – trends over time or ordered values

Use a **line graph** when you want to show how something changes, such as sales over months.

```python
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 135, 190]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (£)")
plt.legend()
plt.grid(True)
plt.show()
```

Useful options:

- `marker="o"` – puts a circle at each data point.
- `label="Sales"` – gives the line a name for the legend.
- `plt.legend()` – displays labels.
- `plt.grid(True)` – adds grid lines.

Other marker examples: `"s"` (square), `"x"` (cross), `"^"` (triangle).

---

## 4. Bar chart – compare categories

Use a **bar chart** to compare separate categories, such as sales by department.

```python
departments = ["IT", "Sales", "HR"]
sales = [500, 800, 350]

plt.figure(figsize=(8, 5))
plt.bar(departments, sales)

plt.title("Sales by Department")
plt.xlabel("Department")
plt.ylabel("Sales (£)")
plt.show()
```

### Horizontal bar chart

Use `barh()` when category names are long or a horizontal chart is easier to read.

```python
plt.barh(departments, sales)
plt.title("Sales by Department")
plt.xlabel("Sales (£)")
plt.ylabel("Department")
plt.show()
```

### Change bar colour

```python
plt.bar(departments, sales, color="steelblue")
```

You can also use a list of colours, one for each bar:

```python
plt.bar(departments, sales, color=["red", "green", "blue"])
```

---

## 5. Scatter graph – relationship between two numeric variables

Use a **scatter graph** to see whether two numerical variables appear related, for example hours studied and test score.

```python
hours = [1, 2, 3, 4, 5]
scores = [45, 50, 62, 70, 82]

plt.figure(figsize=(8, 5))
plt.scatter(hours, scores)

plt.title("Hours Studied vs Test Score")
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.show()
```

Useful options:

```python
plt.scatter(hours, scores, color="red", marker="x", alpha=0.7)
```

- `color` changes the point colour.
- `marker` changes the point shape.
- `alpha` controls transparency: `0` is transparent and `1` is solid.

A scatter graph can show a relationship, but it does not prove that one variable causes the other.

---

## 6. Histogram – distribution of numerical data

Use a **histogram** to show how numerical values are distributed, such as ages or test scores.

```python
ages = [18, 19, 19, 20, 21, 22, 22, 23, 25, 28, 30]

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=5, edgecolor="black")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

- `bins=5` splits the data into five intervals (groups).
- `edgecolor="black"` adds outlines to the bars.
- The vertical axis shows frequency – how many values fall into each interval.

Use a histogram for numerical data, not to compare named categories.

---

## 7. Pie chart – proportions of a whole

Use a **pie chart** to show how categories make up a total.

```python
labels = ["Online", "In-store", "Phone"]
values = [50, 30, 20]

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)

plt.title("Sales by Order Type")
plt.show()
```

- `labels` names each slice.
- `autopct="%1.1f%%"` displays percentages to one decimal place.
- `startangle=90` rotates the starting position.

The values should represent parts of a whole. A pie chart is usually clearest with only a small number of categories.

---

## 8. Box plot – spread and unusual values

Use a **box plot** to summarise the spread of numerical data and help identify possible outliers.

```python
scores = [45, 50, 52, 55, 57, 60, 62, 65, 90]

plt.figure(figsize=(7, 5))
plt.boxplot(scores)

plt.title("Distribution of Scores")
plt.ylabel("Score")
plt.show()
```

A box plot helps show:

- The median (middle value).
- The lower and upper quartiles.
- The spread of the data.
- Possible outliers.

An outlier is a value unusually far from most of the other values. Investigate it rather than automatically deleting it.

---

## 9. Create charts directly from a Pandas DataFrame

You do not always need to create separate Python lists. You can plot DataFrame columns directly.

### Plot one column

```python
df["Sales"].plot()
plt.title("Sales")
plt.xlabel("Record")
plt.ylabel("Sales (£)")
plt.show()
```

### Bar chart from a column

```python
df["Department"].value_counts().plot(kind="bar")
plt.title("Number of Records by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()
```

### Histogram from a column

```python
df["Age"].plot(kind="hist", bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

### Scatter graph from two columns

```python
df.plot(
    kind="scatter",
    x="Hours",
    y="Score"
)

plt.title("Hours vs Score")
plt.show()
```

**Tip:** Pandas plotting uses Matplotlib behind the scenes. You can still use `plt.title()`, `plt.xlabel()`, `plt.ylabel()` and `plt.show()` to customise and display the chart.

---

## 10. Count categories before plotting

A common Task 4A requirement may be to count how many records belong to each category.

```python
counts = df["Department"].value_counts()

counts.plot(kind="bar")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()
```

`value_counts()` counts each different value in the column.

To show percentages instead of counts:

```python
percentages = df["Department"].value_counts(normalize=True) * 100

percentages.plot(kind="bar")
plt.title("Employees by Department (%)")
plt.ylabel("Percentage")
plt.show()
```

---

## 11. Group data, then plot the result

Use `groupby()` to calculate a value for each category before plotting.

```python
average_sales = df.groupby("Department")["Sales"].mean()

average_sales.plot(kind="bar")
plt.title("Average Sales by Department")
plt.xlabel("Department")
plt.ylabel("Average Sales (£)")
plt.show()
```

Other useful calculations:

```python
df.groupby("Department")["Sales"].sum()   # Total per department
df.groupby("Department")["Sales"].mean()  # Average per department
df.groupby("Department")["Sales"].count() # Number of records
df.groupby("Department")["Sales"].max()   # Highest value per department
df.groupby("Department")["Sales"].min()   # Lowest value per department
```

---

## 12. Add a legend – explain multiple data series

A legend tells the reader what each line or data series represents.

```python
months = ["Jan", "Feb", "Mar", "Apr"]
sales_2025 = [100, 120, 140, 160]
sales_2026 = [110, 130, 135, 180]

plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (£)")
plt.legend()
plt.show()
```

The `label=` is set on each plotted series. `plt.legend()` displays those labels.

---

## 13. Improve how a chart looks

These commands are useful for making a chart easier to understand.

```python
plt.title("Monthly Sales", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (£)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

| Command | Purpose |
|---|---|
| `fontsize=16` | Changes text size |
| `plt.grid(True)` | Shows grid lines |
| `plt.xticks(rotation=45)` | Rotates x-axis labels |
| `plt.yticks(rotation=0)` | Sets y-axis label rotation |
| `plt.xlim(0, 10)` | Sets x-axis range |
| `plt.ylim(0, 100)` | Sets y-axis range |
| `plt.tight_layout()` | Adjusts spacing to reduce overlapping |
| `plt.figure(figsize=(10, 6))` | Makes a larger figure |

Only set axis limits when they make sense for the data. Avoid cutting off important values or making a chart misleading.

---

## 14. Save a chart as an image

Use `savefig()` to save a chart, for example as a PNG file.

```python
plt.figure(figsize=(8, 5))
plt.bar(departments, sales)

plt.title("Sales by Department")
plt.xlabel("Department")
plt.ylabel("Sales (£)")

plt.tight_layout()
plt.savefig("sales_chart.png", dpi=300, bbox_inches="tight")
plt.show()
```

- `plt.savefig("sales_chart.png")` saves the chart.
- `dpi=300` gives a higher-resolution image.
- `bbox_inches="tight"` helps include labels around the chart.

**Important:** call `savefig()` before `show()` for reliable results in many environments.

---

## 15. Multiple charts in one figure – subplots

Use `plt.subplots()` when you need more than one chart in the same figure.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(departments, sales)
axes[0].set_title("Sales by Department")
axes[0].set_xlabel("Department")
axes[0].set_ylabel("Sales (£)")

axes[1].plot(months, sales_by_month, marker="o")
axes[1].set_title("Monthly Sales")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Sales (£)")

plt.tight_layout()
plt.show()
```

- `plt.subplots(1, 2)` creates 1 row and 2 columns of charts.
- `axes[0]` refers to the first chart.
- `axes[1]` refers to the second chart.
- With the `axes` object, use `set_title()`, `set_xlabel()` and `set_ylabel()`.

For a 2-by-2 layout, use `plt.subplots(2, 2, figsize=(10, 8))`.

---

## 16. Common chart types – which one should I use?

| Chart | Best used for | Example |
|---|---|---|
| Line (`plot`) | Change or trends | Sales over time |
| Bar (`bar`) | Comparing categories | Sales by department |
| Horizontal bar (`barh`) | Comparing categories with long names | Customers by region |
| Scatter (`scatter`) | Relationship between two numerical variables | Age vs spending |
| Histogram (`hist`) | Distribution of numerical values | Ages or scores |
| Pie (`pie`) | Parts of a whole | Percentage by category |
| Box plot (`boxplot`) | Spread and possible outliers | Salary distribution |

**Quick rule:**
- Comparing categories? Use a **bar chart**.
- Showing change over time? Use a **line graph**.
- Looking for a relationship? Use a **scatter graph**.
- Looking at the distribution of one numerical column? Use a **histogram**.
- Showing proportions of a total? Use a **pie chart**.
- Comparing spread and outliers? Use a **box plot**.

---

## 17. Common mistakes and how to fix them

| Problem | Likely reason | Fix |
|---|---|---|
| `NameError: name 'plt' is not defined` | Matplotlib was not imported | Add `import matplotlib.pyplot as plt` |
| `NameError: name 'df' is not defined` | DataFrame has not been created | Load the CSV into `df` first |
| `KeyError: 'Sales'` | Column name does not exist or spelling/capitalisation differs | Check `df.columns` |
| Chart does not appear | `plt.show()` is missing | Add `plt.show()` at the end |
| Labels overlap | Not enough space | Use `plt.tight_layout()` or rotate labels |
| Bars/line show unexpected values | Wrong column or data type | Check `df.info()` and the selected columns |
| Histogram looks wrong | Data may be text rather than numeric | Check and convert the column appropriately |
| File is not saved where expected | Wrong working directory or path | Check the notebook's current folder and use a clear file path |

---

## 18. A complete example to learn

This example loads a CSV, checks the data, counts categories and creates two charts. Change the file and column names to match your assessment dataset.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data.csv")

# Inspect the data
print(df.head())
print(df.info())

# Count records in each department
department_counts = df["Department"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))
department_counts.plot(kind="bar", color="steelblue")
plt.title("Number of Records by Department")
plt.xlabel("Department")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create a histogram of ages
plt.figure(figsize=(8, 5))
df["Age"].dropna().plot(kind="hist", bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
```

This example assumes the CSV contains columns called `Department` and `Age`. Replace them with the exact column names in your dataset.

---

## 19. Fast revision list – commands to remember

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))  # Create chart area

plt.plot(x, y)              # Line graph
plt.bar(x, y)               # Bar chart
plt.barh(x, y)              # Horizontal bar chart
plt.scatter(x, y)           # Scatter graph
plt.hist(x, bins=10)        # Histogram
plt.pie(values, labels=labels)  # Pie chart
plt.boxplot(x)              # Box plot

plt.title("Title")          # Chart title
plt.xlabel("X label")       # X-axis label
plt.ylabel("Y label")       # Y-axis label
plt.legend()                # Show legend
plt.grid(True)              # Show grid
plt.xticks(rotation=45)     # Rotate x labels
plt.tight_layout()          # Fix spacing
plt.savefig("chart.png")   # Save chart
plt.show()                  # Display chart
```

Pandas plotting shortcuts:

```python
df["Column"].plot(kind="line")
df["Column"].plot(kind="bar")
df["Column"].plot(kind="hist")
df.plot(kind="scatter", x="Column1", y="Column2")
df["Category"].value_counts().plot(kind="bar")
df.groupby("Category")["Number"].mean().plot(kind="bar")
```

---

## 20. Task 4A graph checklist

Before submitting a graph, check:

- [ ] Is this the correct type of chart for the data and question?
- [ ] Does it have a clear, meaningful title?
- [ ] Are both axes labelled?
- [ ] Are units included where needed, such as `£`, `%`, or `Years`?
- [ ] Can the category names and values be read clearly?
- [ ] Is a legend included if there is more than one series?
- [ ] Have you avoided misleading scales or missing information?
- [ ] Does the graph actually use the correct data or filtered results?
- [ ] Have you displayed it with `plt.show()`?
- [ ] If required, have you saved it with `plt.savefig()`?

**Assessment tip:** a graph is not useful just because it runs. It should answer the question, use the correct data, and be clearly labelled. Always use the column names and requirements given in your actual Task 4A brief.
