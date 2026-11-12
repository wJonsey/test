"""
Pandas drills - Riverside Running Club
======================================

Fill in each function so it RETURNS the answer (don't print it).
Then run:  python check_drills.py

Every function receives `df`: the cleaned data with Date already converted.
Look at cheatsheets/4a-coding.md if you get stuck, then close it and try again.
"""

import pandas as pd

ORDER = ["1st", "2nd", "3rd", "Top 10", "Finished"]
MEDALS = ["1st", "2nd", "3rd"]


def load_data(file_name="riverside_results.csv"):
    """Drill 0 (done for you): load the CSV and convert the dates."""
    df = pd.read_csv(file_name)
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    return df


def drill_1_row_count(df):
    """Return how many race results are in the file (an int)."""
    # TODO
    return None


def drill_2_runners(df):
    """Return a list of the runners' names, A to Z, with no repeats."""
    # TODO: unique() and sorted()
    return None


def drill_3_positions(df, runner):
    """Return a Series counting each position for `runner`, in ORDER,
    with 0 for positions they never got."""
    # TODO: filter, value_counts(), reindex(..., fill_value=0)
    return None


def drill_4_prize_totals(df):
    """Return a Series of total prize money per runner, highest first."""
    # TODO: groupby + sum + sort_values
    return None


def drill_5_filter(df, runner, start, end):
    """Return a DataFrame of `runner`'s results between start and end
    (strings like "2025-03-01"), inclusive, in date order."""
    # TODO: one combined mask with &
    return None


def drill_6_event_table(df, runner):
    """Return a crosstab: one row per Event, one column per position in ORDER."""
    # TODO: pd.crosstab(...).reindex(columns=ORDER, fill_value=0)
    return None


def drill_7_average_by_event(df, runner):
    """Return a Series of `runner`'s average prize money per Event, rounded to 2 dp."""
    # TODO
    return None


def drill_8_best_months(df):
    """Return a list of the month numbers (1-12) with the highest total prize money.
    Careful: there may be a tie."""
    # TODO: groupby(df["Date"].dt.month)
    return None


def drill_9_medal_rate(df):
    """Return a Series: % of each runner's races that were 1st, 2nd or 3rd, to 1 dp."""
    # TODO: isin(MEDALS) inside groupby
    return None


def drill_10_money_lines(df, runner):
    """Return a list of strings: `runner`'s running total of prize money
    in date order, formatted like '£1,250.00'."""
    # TODO: sort_values + cumsum + f-string
    return None
