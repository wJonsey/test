"""Task 2 worked example: boundary testing and a hand-checked calculation.

Run it:  python task2_boundary_tests.py
Every line should print PASS. Change `is_valid_weight` to use `<` instead of
`<=` to see what a boundary bug looks like when the tests catch it.
"""


def is_valid_weight(weight):
    """Valid weights are 45 to 150 kg inclusive."""
    return 45 <= weight <= 150


def is_safe_weight_loss(start_weight, end_weight, weeks):
    """True if the weekly loss is within 1% of the starting weight."""
    if weeks <= 0:
        raise ValueError("Weeks must be greater than zero.")
    loss_per_week = (start_weight - end_weight) / weeks
    maximum_per_week = start_weight * 0.01
    return loss_per_week <= maximum_per_week


# (data, expected, type) - expected results written BEFORE running
TEST_CASES = [
    (90, True, "normal"),
    (44, False, "boundary: one below"),
    (45, True, "boundary: on"),
    (46, True, "boundary: one above"),
    (149, True, "boundary: one below"),
    (150, True, "boundary: on"),
    (151, False, "boundary: one above"),
    (-5, False, "erroneous: negative"),
]

for data, expected, kind in TEST_CASES:
    actual = is_valid_weight(data)
    result = "PASS" if actual == expected else "FAIL"
    print(f"{result}: {data:>4} ({kind}) -> expected {expected}, got {actual}")

# 80 kg -> 76 kg in 2 weeks: loss/week = 2.0 kg, maximum = 0.8 kg, so NOT safe
assert is_safe_weight_loss(80, 76, 2) is False
# 80 kg -> 79 kg in 2 weeks: loss/week = 0.5 kg, maximum = 0.8 kg, so safe
assert is_safe_weight_loss(80, 79, 2) is True
print("PASS: hand-calculated weight-loss checks")
