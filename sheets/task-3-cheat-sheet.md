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

## 2. Decompose using abstraction and refinement

Start with the whole problem (abstraction), then repeatedly break it into
smaller, implementable parts (refinement). Justify important decisions.

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

Look for reusable components such as a menu function, date validator, or
filter function rather than repeating the same logic.

---

## 3. Split the problem into three parts

Before writing detailed pseudocode, list what goes **into** the program, what it **does**, and what it **shows**.

| Inputs | Processes | Outputs |
|--------|-----------|---------|
| Menu choice | Load and clean CSV | Table |
| Person | Filter rows | Graph |
| Dates | Count, total, average | "No results" |

Each process becomes **one named function**. Use the same function name in the pseudocode and Python.

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

## 5. Flowchart symbols

Use standard symbols consistently:

| Symbol | Use |
|--------|-----|
| Rounded terminator | Start or End |
| Parallelogram | Input or Output |
| Rectangle | Process or calculation |
| Diamond | Decision, with Yes and No arrows |
| Double-sided rectangle | Calling a named sub-process |

Keep every shape connected. Label both outcomes from every decision and use
the same function names in the flowchart, pseudocode, and code.

---

## 6. Image-style menu pseudocode

The example uses a flag to keep showing the menu until the user chooses a
valid option.

```text
SET not_valid_input TO TRUE

WHILE not_valid_input = TRUE
    SEND "Please choose an option from the list" TO DISPLAY
    SEND "1. Positions" TO DISPLAY
    SEND "2. Prize money" TO DISPLAY
    SEND "3. Exit" TO DISPLAY
    RECEIVE menu_choice (integer) FROM KEYBOARD

    IF menu_choice = 1 THEN
        SEND "Positions selected" TO DISPLAY
        SET not_valid_input TO FALSE
    ELSE IF menu_choice = 2 THEN
        SEND "Prize money selected" TO DISPLAY
        SET not_valid_input TO FALSE
    ELSE IF menu_choice = 3 THEN
        SEND "Goodbye" TO DISPLAY
        SET not_valid_input TO FALSE
    ELSE
        SEND "That is not a valid choice" TO DISPLAY
    END IF
END WHILE

RETURN menu_choice
```

For a shorter design, use:

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

---

## 7. Get an athlete from a numbered list

Load the data, create a list of unique names, and validate the user's number.

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

## 8. Get and validate dates

Check the format before comparing dates. Reject a range where the end is
before the start.

```text
FUNCTION get_dates()
    RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
    RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD

    WHILE start_date is not a valid date OR
          end_date is not a valid date OR
          end_date is before start_date
        SEND "Enter a valid date range" TO DISPLAY
        RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
        RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD
    END WHILE

    CONVERT start_date TO a date
    CONVERT end_date TO a date
    RETURN start_date, end_date
END FUNCTION
```

---

## 9. Filter rows and count results

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

> ⚠️ Never `RETURN` inside the loop. It stops at the first row that doesn't match.

---

## 10. Communicate the design

The design must be detailed enough for a client to make decisions and for a
third party to build the solution. Use:

- technical vocabulary accurately;
- consistent names across flowcharts, pseudocode, and code;
- written explanations alongside diagrams;
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

## 11. Top mistakes

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
