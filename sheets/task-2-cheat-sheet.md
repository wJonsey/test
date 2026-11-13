# T Level DSD – Task 2 Testing and Fixing Code Cheat Sheet

A practical revision guide to planning tests, identifying errors, fixing
faults and proving that a program meets its requirements.

> **Important:** High marks come from the quality of the testing evidence, not
> simply from finding lots of bugs. Always predict the result before running
> a test, record what actually happened, and retest after every fix.

**Assessment weighting:** 21 marks — Testing 9, Understanding 3, Fixing the
solution 9.

---

## 1. What is testing?

Testing checks whether a program:

- meets each requirement;
- accepts valid input;
- rejects invalid input safely;
- produces the correct result;
- gives useful messages rather than crashing.

Testing is not just running the program once. It is a planned comparison
between an **expected result** and an **actual result**.

Use this cycle for every test:

**Predict → Run → Compare → Record → Fix → Retest**

Write the expected result before running the program. Otherwise it is easy to
change your explanation after seeing the output.

---

## 2. Test the important kinds of data

Suppose a valid weight is from 45 to 150 kg inclusive.

| Test type | Example | What it checks |
|---|---:|---|
| Normal | `90` | A typical valid value |
| Lower boundary | `44`, `45`, `46` | Just below, on and just above the lower limit |
| Upper boundary | `149`, `150`, `151` | Just below, on and just above the upper limit |
| Invalid extreme | `-999`, `999` | Very unrealistic values |
| Erroneous input | `"abc"`, blank, `1.5` | Wrong type, missing or malformed data |

For an inclusive range, the expected result is:

| Value | 44 | 45 | 46 | 90 | 149 | 150 | 151 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Result | Reject | Accept | Accept | Accept | Accept | Accept | Reject |

Boundary tests are especially important because mistakes often occur in
comparisons such as `>` versus `>=`.

---

## 3. Test against the requirements

Turn every requirement into a testable statement.

| Requirement | Test purpose | Test data | Expected result |
|---|---|---|---|
| Accept weights from 45 to 150 kg | Check both valid limits | `45`, `150` | Accepted |
| Reject weights outside the range | Check invalid boundaries | `44`, `151`, `-999` | Rejected |
| Handle text input | Check robustness | `"abc"` | Friendly error; no crash |
| Calculate weekly loss correctly | Check calculation | `80`, `76`, `2` weeks | `2.0 kg` per week |

Explain why each test is needed. A list of random inputs is weaker evidence
than a test linked to a requirement.

---

## 4. Recognise the three main error types

| Error type | What it means | Example |
|---|---|---|
| Syntax | Python cannot understand the code | Missing `:` or closing `)` |
| Runtime | The program starts but crashes while running | Converting `"abc"` to a number |
| Logic | The program runs but gives the wrong answer | Using `>` instead of `>=` |

A useful order for investigating a problem:

1. **Does the program start?** Look for a syntax error.
2. **Does it crash while running?** Look for a runtime error and traceback.
3. **Is the answer correct?** Check for a logic error using hand calculations.

Logic errors are only found when you compare the output with a prediction.

---

## 5. Use a test log

Record one row for every test.

| Test and purpose | Data (type) | Expected | Actual | Line and error type | Fix and retest |
|---|---|---|---|---|---|
| Upper limit | `150` (boundary) | Accepted | Rejected | Line 40, logic | Changed comparison; retested `149`, `150`, `151` |
| Weeks as a decimal | `1.5` (valid) | Accepted | Rejected | Line 18, logic | Used `float()` in validation; retested `1.5`, `2`, `"abc"` |

Include evidence such as labelled screenshots, output, or code lines. Give
each test a number so an assessor can match the evidence to the log.

For each failed test, record:

1. the requirement that failed;
2. the expected and actual results;
3. the error type and line;
4. the change made and why it fixes the cause;
5. the original test and related boundary cases after the fix.

---

## 6. Work out expected answers by hand

Example: a person changes from 80 kg to 76 kg in 2 weeks. The recommended
maximum loss is 1% of the starting weight per week.

| Step | Working | Answer |
|---|---|---:|
| Total weight to lose | `80 - 76` | `4.0 kg` |
| Weight loss per week | `4 / 2` | `2.0 kg` |
| Maximum per week | `80 * 0.01` | `0.8 kg` |
| Is it allowed? | `2.0 > 0.8` | **No** |

Hand calculations provide a reliable expected result for testing program
logic.

---

## 7. Validate numeric input safely

Use a loop so the user is asked again until valid data is entered.

```python
while True:
    try:
        weight = float(input("Enter your weight (45-150 kg): "))

        if 45 <= weight <= 150:
            break

        print("Weight must be between 45 and 150 kg.")
    except ValueError:
        print("Please enter a number.")
```

Test this with:

- a normal valid value such as `90`;
- `44`, `45`, `46`, `149`, `150`, and `151`;
- a negative value;
- text and a blank input.

The program should not expose a traceback to an ordinary user.

---

## 8. Fixes and retesting

When a test fails:

1. Describe the requirement that was not met.
2. Identify whether the fault is syntax, runtime or logic.
3. Find the cause rather than hiding the symptom.
4. Make the smallest suitable code change.
5. Retest the original failing value.
6. Retest nearby values and related invalid input.

For example, if `150` is incorrectly rejected, changing the comparison from
`weight < 150` to `weight <= 150` should be followed by tests for `149`,
`150` and `151`.

Do not silently change the requirement to make a failed test pass.

---

## 9. Common testing mistakes

| Mistake | Why it is weak | Better approach |
|---|---|---|
| Testing only normal values | Boundary and invalid faults remain hidden | Test below, on and above every limit |
| Writing “works as intended” | It does not show what was checked | Record expected and actual output |
| Finding a bug without fixing it | The requirement is still unmet | Fix the cause and retest |
| Fixing without a retest | The fix may create another fault | Repeat the original and related tests |
| Leaving debug `print()` statements | Final output becomes confusing | Remove temporary diagnostics |
| Showing technical tracebacks | Users cannot understand them | Catch specific errors and show a useful message |
| Using screenshots as expected results | Screenshots show output, not prediction | Calculate and write expected values first |

---

## 10. A complete test example

For a program that calculates weight loss:

| Test | Input | Expected result | Why this test matters |
|---:|---|---|---|
| 1 | `80`, `76`, `2` | `2.0 kg` per week; allowed: no | Normal calculation |
| 2 | `80`, `79.2`, `1` | `0.8 kg`; allowed: yes | Exact calculation boundary |
| 3 | Starting weight `45` | Accepted | Lower valid boundary |
| 4 | Starting weight `44.9` | Rejected | Just below lower boundary |
| 5 | Starting weight `150` | Accepted | Upper valid boundary |
| 6 | Starting weight `150.1` | Rejected | Just above upper boundary |
| 7 | Weeks `0` | Rejected | Prevents division by zero |
| 8 | Weight `"abc"` | Friendly error; no crash | Erroneous input |

After running each case, fill in the actual result, any fault, the fix and
the retest evidence.

---

## 11. Sentences for evaluation

- “This boundary test uses one value below, on and one value above the limit.”
- “The actual result did not match my prediction, so this was a logic error.”
- “I changed `[code]` on line `[number]`, then retested `[values]`.”
- “This test checks the requirement that `[requirement]`.”
- “The further action is `[action]` because the actual result `[problem]`.”

---

## 12. Fast revision list

Remember:

1. Test normal, boundary, invalid extreme and erroneous data.
2. Test just below, on and just above every limit.
3. Write the expected result before running the program.
4. Compare expected and actual results.
5. Identify syntax, runtime and logic errors correctly.
6. Record the line, fault, fix and retest.
7. Test the original failure again after every fix.
8. Remove debug output before submission.

---

## 13. Task 2 testing checklist

- [ ] Every requirement has at least one linked test.
- [ ] Normal values are included.
- [ ] Lower and upper boundary values are included.
- [ ] Invalid extreme and erroneous inputs are included.
- [ ] Expected results were written before running.
- [ ] Actual results are recorded accurately.
- [ ] Every fault has an error type and line number.
- [ ] Fixes explain the cause, not just the changed line.
- [ ] Every fix has been retested.
- [ ] Evidence is labelled and easy to match to the test log.
- [ ] No debug prints or tracebacks remain in final output.

**Assessment tip:** strong testing demonstrates what was tested, why it was
tested, what happened, what changed and how the fix was proved.
