"""
Marks your drills.py.  Run:  python check_drills.py
Each drill is checked against the right answer. Fix any ✗ and run it again.
"""

import pandas as pd

import drills

GREEN, RED, GREY, END = "\033[92m", "\033[91m", "\033[90m", "\033[0m"


def series_equal(got, expected):
    """True if `got` is a pandas Series with the same index and values."""
    return (isinstance(got, pd.Series)
            and list(got.index) == list(expected.index)
            and [round(float(v), 2) for v in got.values] == expected.values.tolist())


def check(number, description, test):
    """Run one test, print a tick or cross, and return 1 if it passed."""
    try:
        passed = test()
    except Exception as error:  # show the learner what went wrong, then carry on
        print(f"{RED}✗ Drill {number}{END} {description}  {GREY}({type(error).__name__}: {error}){END}")
        return 0
    mark = f"{GREEN}✓" if passed else f"{RED}✗"
    print(f"{mark} Drill {number}{END} {description}")
    return 1 if passed else 0


def main():
    """Load the data once and run every check."""
    df = drills.load_data()
    tests = [
        (1, "row count", lambda: drills.drill_1_row_count(df) == 24),
        (2, "runners A to Z", lambda: drills.drill_2_runners(df)
            == ["Amara Okafor", "Ben Hughes", "Chloe Martin", "Dev Patel"]),
        (3, "Ben Hughes positions, with zeros", lambda: series_equal(
            drills.drill_3_positions(df, "Ben Hughes"),
            pd.Series([1, 1, 1, 2, 1], index=drills.ORDER))),
        (4, "prize totals, highest first", lambda: series_equal(
            drills.drill_4_prize_totals(df),
            pd.Series([825, 570, 405, 355],
                      index=["Amara Okafor", "Dev Patel", "Ben Hughes", "Chloe Martin"]))),
        (5, "Chloe Martin, March to June", lambda: (
            lambda r: r is not None and list(r["Position"]) == ["Finished", "1st", "Top 10"]
            and list(r["Prize Money"]) == [0, 150, 0]
        )(drills.drill_5_filter(df, "Chloe Martin", "2025-03-01", "2025-06-30"))),
        (6, "Dev Patel crosstab", lambda: (
            lambda t: t is not None and list(t.columns) == drills.ORDER
            and t.loc["10K"].tolist() == [1, 1, 0, 1, 0]
            and t.loc["5K"].tolist() == [1, 0, 1, 0, 0]
        )(drills.drill_6_event_table(df, "Dev Patel"))),
        (7, "Amara average per event", lambda: (
            lambda s: s is not None and round(float(s["10K"]), 2) == 148.33
            and round(float(s["5K"]), 2) == 95.0
        )(drills.drill_7_average_by_event(df, "Amara Okafor"))),
        (8, "best months (a tie!)", lambda: sorted(drills.drill_8_best_months(df)) == [2, 8]),
        (9, "medal rate %", lambda: (
            lambda s: s is not None and {k: round(float(v), 1) for k, v in s.items()}
            == {"Amara Okafor": 85.7, "Ben Hughes": 50.0, "Chloe Martin": 66.7, "Dev Patel": 80.0}
        )(drills.drill_9_medal_rate(df))),
        (10, "Amara running total in £", lambda: drills.drill_10_money_lines(df, "Amara Okafor")
            == ["£150.00", "£270.00", "£270.00", "£520.00", "£600.00", "£675.00", "£825.00"]),
    ]
    score = sum(check(*t) for t in tests)
    print(f"\n{score} / {len(tests)} correct")
    if score == len(tests):
        print(f"{GREEN}All done. Now try writing them again tomorrow without looking.{END}")


if __name__ == "__main__":
    main()
