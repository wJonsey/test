# Task 2 · Testing and Fixing Code

**21 marks** · Testing 9 · Understanding 3 · Fix 9

> **The big idea:** top marks come from *good tests*, not from finding lots of bugs.

### How to use this sheet

For each input in your program:

1. Choose a normal value.
2. Test just below, on and just above every limit.
3. Try an invalid value.
4. Write what you expect **before** running the program.
5. Compare the result, record any fault, fix it and test again.

---

## 1. Test five kinds of data

| Type | Meaning | Example (valid: 45 to 150) |
|------|---------|----------------------------|
| **Valid normal** | Typical valid value | `90` |
| **Valid extreme** | Valid but at an unusual extreme | `45` or `150` |
| **Invalid normal** | Normally invalid value | `44` or `151` |
| **Invalid extreme** | Very far outside the valid range | `-999` or `999` |
| **Erroneous** | Wrong type, blank, or malformed | `"abc"` · blank · `1.5` |

| Value | 44 | 45 | 46 | 90 | 149 | 150 | 151 |
|:-----:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|
| Result | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

Use an ordinary value as well as valid and invalid extremes. Erroneous data
could include `"abc"`, blank input, the wrong date format, or a missing file.

---

## 2. Name the error

Use these simple questions in order: **Does the program start? Does it crash? Is the answer correct?**

```mermaid
flowchart TD
    START(["Start"]) --> A{"Does it start?"}
    A -->|No| S["SYNTAX<br/>missing : ) or quote"]
    A -->|Yes| B{"Does it crash?"}
    B -->|Yes| R["RUNTIME<br/>NameError, ValueError"]
    B -->|No| C{"Answer matches<br/>your prediction?"}
    C -->|No| L["LOGIC<br/>wrong operator or formula"]
    C -->|Yes| P["PASS"]
    S --> END(["End"])
    R --> END
    L --> END
    P --> END
```

| Error | What it means | Example |
|-------|---------------|---------|
| Syntax | Python cannot understand the code | Missing `:` or closing `)` |
| Runtime | The program starts but crashes while running | Converting `"abc"` to a number |
| Logic | The program runs but gives the wrong answer | Using `>` instead of `>=` |

---

## 3. Test against the requirements

Before testing, turn each requirement into a testable statement:

| Requirement | Test purpose | Data | Expected result |
|-------------|--------------|------|-----------------|
| Accept 45–150 kg | Check lower and upper limits | `45`, `150` | Accepted |
| Reject outside range | Check invalid extremes | `44`, `151`, `-999` | Rejected |
| Handle text input | Check robustness | `"abc"` | Friendly error; no crash |

Explain why each test is needed. A list of inputs without a purpose is weaker
evidence.

---

## 4. Follow the loop every time

**Predict → Run → Compare → Record → Fix → Retest**

- Write the expected result **before** running.
- Never write "works as intended" if it is wrong.
- Never record a fix without a **retest**.

---

## 5. Test log (one row per test)

| Test and purpose | Data (type) | Expected | Actual | Line + error type | Further action, fix + retest |
|------|-------------|----------|--------|-------------------|--------------|
| Upper limit: check boundary | `150` (valid extreme) | Accepted | "Not valid" | Line 40, logic | Changed comparison; retested 149, 150, 151 ✅ |

Annotate evidence such as screenshots, output, or code lines. Label each item
with the test number so an assessor can match the evidence to the log.

---

## 6. Requirements, fixes, and retesting

For each failure:

1. State the requirement that failed.
2. Describe the actual result and identify the error type.
3. Explain the remedial action and why it fixes the cause.
4. Retest the original case and related cases.
5. Record whether the requirement is now met.

Do not silently change the requirement to make a failed test pass.

---

## 7. Work out answers by hand

80 kg → 76 kg in 2 weeks, max loss 1% per week:

| Step | Working | Answer |
|------|---------|--------|
| Lose in total | 80 − 76 | 4.0 kg |
| Per week | 4 ÷ 2 | 2.0 kg |
| Maximum per week | 80 × 0.01 | 0.8 kg |
| Allowed? | 2.0 > 0.8 | **No** |

---

## Sentences to reuse

- "The boundary test used one value below, on, and one value above the limit."
- "The actual result did not match my prediction, so this was a logic error."
- "I changed `[code]` on line `[number]`, then retested `[values]`."
- "This test checks the requirement that `[requirement]`."
- "The further action is `[action]` because the actual result `[problem]`."

---

## Final check

- [ ] Normal, boundary **and** erroneous data
- [ ] Valid extreme, invalid extreme, and erroneous data included
- [ ] Every test has a purpose linked to a requirement
- [ ] Expected result written first
- [ ] Actual result compared with expected
- [ ] Error type + line number for every fault
- [ ] Further actions are described
- [ ] Every fix has a retest
- [ ] Evidence is annotated and labelled
- [ ] No debug prints, no tracebacks
