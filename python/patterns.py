"""
The six Task 4a patterns, working on riverside_results.csv.
Run:  python patterns.py
Change things and run again to see what happens (e.g. try a runner who doesn't exist).
"""

import pandas as pd

FILE = "riverside_results.csv"
ORDER = ["1st", "2nd", "3rd", "Top 10", "Finished"]


# 1 · Load safely ------------------------------------------------------------
def load_data(file_name):
    """Read the CSV, or return None with a friendly message if it's missing."""
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        print(f"Can't find {file_name}. Put it in the same folder as this program.")
        return None
    # 2 · Dates: dd/mm/yyyy, unreadable dates become NaT instead of crashing
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    return df


# 3 · Filter with one mask -----------------------------------------------------
def filter_results(df, runner, start, end):
    """Return a NEW DataFrame of one runner's results between two dates."""
    mask = (df["Runner"] == runner) & df["Date"].between(start, end)
    return df.loc[mask].copy()


# 4 · Count, never None --------------------------------------------------------
def count_positions(results):
    """Count every position in ORDER, with 0 for any not achieved."""
    return results["Position"].value_counts().reindex(ORDER, fill_value=0)


# 5 · Compare groups -----------------------------------------------------------
def compare_events(results):
    """Positions per event, side by side."""
    return pd.crosstab(results["Event"], results["Position"]).reindex(columns=ORDER, fill_value=0)


# 6 · Input loop ---------------------------------------------------------------
def get_menu_choice(title, options):
    """Show a numbered menu; keep asking until a valid number is entered."""
    while True:
        print(f"\n{title}")
        for number, option in enumerate(options, start=1):
            print(f"  {number}. {option}")
        answer = input("Choice: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print(f"Please enter a number from 1 to {len(options)}.")


def main():
    """Walk through each pattern."""
    df = load_data(FILE)
    if df is None:
        return

    runners = sorted(df["Runner"].unique())
    choice = get_menu_choice("Pick a runner", runners)
    runner = runners[choice - 1]

    results = filter_results(df, runner, "2025-01-01", "2025-12-31")
    if results.empty:
        print("No results for that runner in 2025.")
        return

    print(f"\n{runner}, 2025")
    for position, count in count_positions(results).items():
        print(f"  {position:<9}{count:>3}")
    print(f"  Prize money: £{results['Prize Money'].sum():,.2f}")
    print("\nBy event:")
    print(compare_events(results).to_string())


if __name__ == "__main__":
    main()
