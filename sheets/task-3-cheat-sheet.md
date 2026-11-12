# Task 3 · Designing a Solution

**18 marks** · Decomposition 9 · Logic and conventions 6 · Communication 3

> **The big idea:** another developer should be able to build your program from your design alone.

---

## 1. Write the steps in the right order

Pseudocode is structured English. It explains what the program does without requiring perfect Python syntax.

Use this order:

1. Get the input.
2. Check that the input is valid.
3. Process or calculate the result.
4. Display the output.

Simple example:

```text
RECEIVE name FROM KEYBOARD
SEND "Hello " + name TO DISPLAY
```

Use clear indentation so it is obvious which instructions belong inside a condition or loop.

---

## 2. Split the problem into three parts

Before writing detailed pseudocode, list what goes **into** the program, what it **does**, and what it **shows**.

| Inputs | Processes | Outputs |
|--------|-----------|---------|
| Menu choice | Load and clean CSV | Table |
| Person | Filter rows | Graph |
| Dates | Count, total, average | "No results" |

Each process becomes **one named function**. Use the same function name in the pseudocode and Python.

---

## 3. Pseudocode words

| Do this | Write this |
|---------|-----------|
| Input | `RECEIVE choice FROM KEYBOARD` |
| Output | `SEND "Hello" TO DISPLAY` |
| Assign | `SET total TO 0` |
| Choose | `IF ... THEN ... ELSE ... END IF` |
| Repeat | `WHILE ... END WHILE` · `FOR EACH row IN data ... NEXT row` |
| Function | `FUNCTION get_dates() ... RETURN start, end` |

Pseudocode is structured English: it explains the logic without needing perfect Python syntax. Indent everything inside an `IF` or loop.

---

## 4. Validation loop: ask until valid

Ask for the value, check it, and repeat if it is wrong.

```text
FUNCTION get_menu_choice()
    RECEIVE choice FROM KEYBOARD

    WHILE choice is not between 1 and 4
        SEND "Enter a number from 1 to 4" TO DISPLAY
        RECEIVE choice FROM KEYBOARD
    END WHILE

    RETURN choice
END FUNCTION
```

Dates: check the **format**, convert the values, then check **end is not before start**.

---

## 5. Counting loop: decide after the loop

```text
FUNCTION count_results(data, selected_name, start_date, end_date)
    SET count TO 0
    SET total TO 0

    FOR EACH row IN data
        IF row matches name AND date range THEN
            SET count TO count + 1
            SET total TO total + row.PrizeMoney
        END IF
    NEXT row

    IF count = 0 THEN
        SEND "No results" TO DISPLAY
    ELSE
        SEND count, total TO DISPLAY
    END IF
END FUNCTION
```

> ⚠️ Never `RETURN` inside the loop. It stops at the first row that doesn't match.

---

## Top mistakes

| ❌ Don't | ✅ Do |
|---------|------|
| Mix input, processing and output together | Keep each step clear |
| Use vague instructions such as "check it" | State exactly what is being checked |
| Ask "is it a string?" | Check the name **is in the list** |
| Forget `SET count TO 0` | Initialise before the loop |
| Rename functions between pseudocode and code | Keep one name each |

---

## Final check

- [ ] Inputs, processes and outputs listed
- [ ] Named functions included
- [ ] Every decision has a clear true/false outcome
- [ ] Validation loops repeat
- [ ] Counters are initialised before loops
- [ ] "No results" handled after the loop
- [ ] The pseudocode has a clear beginning and ending
