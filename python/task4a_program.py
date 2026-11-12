"""Task 4a worked example: a menu-driven race results explorer using pandas.

Run it from this folder:  python task4a_program.py
Needs:                    pip install pandas matplotlib
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path(__file__).with_name("results.csv")  # only ever read this file
DATE_FORMAT = "%d/%m/%Y"
REQUIRED_COLUMNS = ["Date", "Runner", "Event", "Position", "Prize Money"]
POSITION_ORDER = ["1st", "2nd", "3rd", "Top 10", "Finished"]
OPTIONS = [
    "Show finishing positions",
    "Show prize money",
    "Show positions graph",
    "Exit",
]


# ---------------------------------------------------------------- loading
def load_data(filename):
    """Load and clean the CSV. Return a DataFrame, or None if it can't be used."""
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Can't find {Path(filename).name}. Put it in the same folder.")
        return None
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:
        print(f"Could not read the data file: {error}")
        return None

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        print(f"The data file is missing column(s): {', '.join(missing)}")
        return None

    df["Date"] = pd.to_datetime(df["Date"], format=DATE_FORMAT, errors="coerce")
    df["Prize Money"] = pd.to_numeric(df["Prize Money"], errors="coerce").fillna(0)

    rows_before = len(df)
    df = df.dropna(subset=["Date", "Runner"])
    dropped = rows_before - len(df)
    if dropped:
        print(f"Note: ignored {dropped} row(s) with a missing or invalid date/name.")
    return df


# ------------------------------------------------------------------ input
def get_menu_choice(title, options):
    """Show a numbered menu and return a valid choice (1 to len(options))."""
    while True:
        print(f"\n{title}")
        for number, option in enumerate(options, start=1):
            print(f"  {number}. {option}")

        answer = input("Choice: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print(f"Please enter a number from 1 to {len(options)}.")


def get_person(df):
    """Show numbered runner names and return the one the user picks."""
    names = sorted(df["Runner"].unique())
    while True:
        print("\nRunners")
        for number, name in enumerate(names, start=1):
            print(f"  {number}. {name}")

        answer = input("Choose a runner: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(names):
            return names[int(answer) - 1]
        print(f"Please enter a number from 1 to {len(names)}.")


def get_dates():
    """Return a valid (start, end) date pair entered as dd/mm/yyyy."""
    while True:
        try:
            start = pd.to_datetime(
                input("Start date (dd/mm/yyyy): ").strip(), format=DATE_FORMAT
            )
            end = pd.to_datetime(
                input("End date (dd/mm/yyyy): ").strip(), format=DATE_FORMAT
            )
        except ValueError:
            print("Use the date format dd/mm/yyyy, for example 31/12/2025.")
            continue

        if end >= start:
            return start, end
        print("The end date must not be before the start date.")


# ------------------------------------------------------------- processing
def filter_results(df, name, start, end):
    """Return a copy of the rows for one runner between two dates (inclusive)."""
    mask = (df["Runner"] == name) & df["Date"].between(start, end)
    return df.loc[mask].copy()


def get_position_counts(results):
    """Return the count for every position, in a fixed order (missing = 0)."""
    return results["Position"].value_counts().reindex(POSITION_ORDER, fill_value=0)


def get_prize_summary(results):
    """Return (races, total prize money, average prize money)."""
    return len(results), results["Prize Money"].sum(), results["Prize Money"].mean()


# ----------------------------------------------------------------- output
def report_positions(results):
    """Print an aligned table of finishing positions."""
    if results.empty:
        print("No results found for that runner and date range.")
        return

    print("\nFinishing positions")
    print("-" * 22)
    for position, count in get_position_counts(results).items():
        print(f"  {position:<10}{count:>4}")


def report_prize_money(results):
    """Print the total and average prize money."""
    if results.empty:
        print("No results found for that runner and date range.")
        return

    races, total, average = get_prize_summary(results)
    print("\nPrize money")
    print("-" * 22)
    print(f"  Races:    {races}")
    print(f"  Total:    £{total:,.2f}")
    print(f"  Average:  £{average:,.2f}")


def plot_positions(results, name):
    """Display a labelled bar chart of finishing positions."""
    if results.empty:
        print("No results to plot for that runner and date range.")
        return

    get_position_counts(results).plot(kind="bar", rot=0)
    plt.title(f"Finishing positions - {name}")
    plt.xlabel("Position")
    plt.ylabel("Number of races")
    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------------- main
def main():
    """Load the data, then show the menu until the user chooses Exit."""
    data = load_data(DATA_FILE)
    if data is None:
        return

    while True:
        choice = get_menu_choice("Main menu", OPTIONS)
        if choice == len(OPTIONS):
            print("Goodbye.")
            break

        name = get_person(data)
        start, end = get_dates()
        results = filter_results(data, name, start, end)

        if choice == 1:
            report_positions(results)
        elif choice == 2:
            report_prize_money(results)
        else:
            plot_positions(results, name)


if __name__ == "__main__":
    main()
