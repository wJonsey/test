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

## 2. Break the problem into functions

Start with the whole problem, then break it into smaller tasks that can each
be written as one function.

```text
Results system
  INPUTS
    get_menu_choice()
    get_athlete()
    get_dates()
  PROCESSING
    load_data()
    filter_results()
    calculate_summary()
  OUTPUTS
    show_table()
    show_graph()
    show_no_results()
```

Reusable functions such as a menu function, date validator, or filter
function prevent the same logic being copied in several places.

---

## 3. Split the problem into three parts

Before writing detailed pseudocode, list what goes **into** the program, what it **does**, and what it **shows**.

| Inputs | Processes | Outputs |
|--------|-----------|---------|
| Menu choice | Load and clean CSV | Table |
| Person | Filter rows | Graph |
| Dates | Count, total, average | "No results" |

Each process should be covered by a **named function**. Related steps may be
grouped together, but use the same function name in the pseudocode and Python.

---

## 4. Pseudocode words

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

## 5. Menu pseudocode

Ask for a choice and repeat the question until the answer is valid.

```text
FUNCTION get_menu_choice()
    SEND "1. Positions" TO DISPLAY
    SEND "2. Prize money" TO DISPLAY
    SEND "3. Exit" TO DISPLAY
    RECEIVE choice (integer) FROM KEYBOARD
    WHILE choice is not between 1 and 3
        SEND "Enter a number from 1 to 3" TO DISPLAY
        RECEIVE choice (integer) FROM KEYBOARD
    END WHILE
    RETURN choice
END FUNCTION
```

---

## 6. Get an athlete from a numbered list

Create a list of unique names and validate the user's number.

```text
FUNCTION get_athlete(dataframe)
    SET athlete_names TO unique values from dataframe["Athlete"]
    SEND "Here is a list of athletes in the data" TO DISPLAY

    FOR EACH name IN athlete_names
        SEND position number and name TO DISPLAY
    NEXT name

    RECEIVE user_selection (integer) FROM KEYBOARD
    WHILE user_selection is less than 1 OR
          user_selection is greater than length of athlete_names
        SEND "Choose a number from the list" TO DISPLAY
        RECEIVE user_selection (integer) FROM KEYBOARD
    END WHILE

    SET chosen_athlete TO athlete_names[user_selection - 1]
    RETURN chosen_athlete
END FUNCTION
```

Do not ask whether the name is a string. Check that the selected number is in
range and then obtain the name from the list.

---

## 7. Get and validate dates

Check the format before comparing dates. Reject a range where the end is
before the start.

```text
FUNCTION get_dates()
    RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
    RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD

    WHILE start_date or end_date is not in dd/mm/yyyy format OR
          start_date or end_date is not a valid date
        SEND "Enter a valid date range" TO DISPLAY
        RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
        RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD
    END WHILE

    CONVERT start_date TO a date
    CONVERT end_date TO a date

    WHILE end_date is before start_date
        SEND "Enter a valid date range" TO DISPLAY
        RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
        RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD

        WHILE start_date or end_date is not in dd/mm/yyyy format OR
              start_date or end_date is not a valid date
            SEND "Enter a valid date range" TO DISPLAY
            RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
            RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD
        END WHILE

        CONVERT start_date TO a date
        CONVERT end_date TO a date
    END WHILE

    RETURN start_date, end_date
END FUNCTION
```

---

## 8. Filter rows and count results

Use inclusive comparisons so results on both dates are included.

```text
FUNCTION count_results(data, selected_name, start_date, end_date)
    SET count TO 0
    SET total TO 0

    FOR EACH row IN data
        IF row.Date >= start_date AND row.Date <= end_date AND
           row.Athlete = selected_name THEN
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

> ⚠️ Never `RETURN` the result inside the loop. It stops at the first
> matching row and prevents the remaining rows from being processed.

---

## 9. Communicate the design

The design must be detailed enough for a client to make decisions and for a
third party to build the solution. Use:

- technical vocabulary accurately;
- consistent names across pseudocode and code;
- written explanations alongside the pseudocode;
- inputs, outputs, data types, and data structures;
- sequence, selection, and iteration;
- reasons for important choices and their effects.

Example:

```text
SET count (integer) TO 0
SET total_prize (real) TO 0.0
SET athlete_names (list of strings) TO unique athlete names
```

---

## 10. Top mistakes

| ❌ Don't | ✅ Do |
|---------|------|
| Mix input, processing and output together | Keep each step clear |
| Use vague instructions such as "check it" | State exactly what is being checked |
| Ask "is it a string?" | Check the name **is in the list** |
| Use an unchecked athlete number | Check it is between 1 and the list length |
| Compare unparsed date text | Validate and convert dates first |
| Forget `SET count TO 0` | Initialise before the loop |
| Rename functions between pseudocode and code | Keep one name each |

---

## Example main sequence

```text
FUNCTION main()
    IMPORT data-handling library
    READ "Task3a_data.csv"
    SET dataframe TO the data
    SET dataframe["Date"] TO dates parsed as dd/mm/yyyy

    SET chosen_athlete TO get_athlete(dataframe)
    SET start_date, end_date TO get_dates()
    CALL count_results(dataframe, chosen_athlete, start_date, end_date)
END FUNCTION

CALL main()
```

This makes the order clear: load data, get valid inputs, process the rows,
then display the result.

---

## Final check

- [ ] Inputs, processes and outputs listed
- [ ] Problem refined from a whole system into smaller components
- [ ] Named functions included
- [ ] Reusable components identified
- [ ] Every decision has a clear true/false outcome
- [ ] Sequence, selection, and iteration are all shown
- [ ] Validation loops repeat
- [ ] Counters are initialised before loops
- [ ] "No results" handled after the loop
- [ ] Athlete names come from a numbered, validated list
- [ ] Dates use `dd/mm/yyyy` and end is not before start
- [ ] Start and end dates are included in the filter
- [ ] Data types and structures are clear
- [ ] Design is understandable to both technical and non-technical readers
- [ ] Important design decisions are justified
- [ ] The pseudocode has a clear beginning and ending
