# T Level DSD – Task 3 Designing a Solution Cheat Sheet

A practical revision guide to decomposition, flowcharts, pseudocode,
validation, data structures and communicating a design clearly enough for
another developer to build.

> **Important:** A design is not just a list of features. It should show the
> inputs, processing, outputs, sequence, selection, iteration, data types and
> reasons for important decisions.

**Assessment weighting:** 18 marks — Decomposition 9, Logic and conventions 6,
Communication 3.

---

## 1. What is a design?

A design is a plan for a program before implementation. It should allow:

- a client to understand what the solution will do;
- another developer to build the solution;
- decisions and assumptions to be checked before coding;
- the final program to be compared with the requirements.

Use consistent names in the design and the Python code. If the design calls a
function `get_dates()`, use the same name when implementing it.

---

## 2. Separate inputs, processes and outputs

Before writing detailed pseudocode, list what goes **into** the program, what
it **does**, and what it **shows**.

| Inputs | Processes | Outputs |
|---|---|---|
| Menu choice | Load and clean CSV | Labelled table |
| Person or athlete | Filter rows | Graph |
| Start and end dates | Count, total and average | “No results” message |

Each important process should be covered by a named function.

---

## 3. Decompose the problem into functions

Start with the whole problem, then break it into smaller tasks.

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

Good functions have one clear responsibility. Reusable functions prevent the
same validation or filtering logic being copied in several places.

---

## 4. Flowchart symbols

| Shape | Use for |
|---|---|
| Rounded rectangle | Start and End |
| Parallelogram | Every input and output |
| Rectangle | Assignment, calculation or other process |
| Diamond | A decision with true/false outcomes |
| Double-sided rectangle | Calling a function or sub-process |

Flowcharts should:

- have a clear beginning and ending;
- connect every shape;
- show the direction of flow;
- label both branches of a decision `Yes` and `No`;
- use one symbol for each meaningful step.

---

## 5. Pseudocode structure

Pseudocode is structured English. It explains the algorithm without requiring
perfect Python syntax.

Use this general order:

1. Get input.
2. Check that the input is valid.
3. Process or calculate the result.
4. Display the output.

```text
RECEIVE name FROM KEYBOARD
WHILE name is not valid
    SEND "Enter a valid name" TO DISPLAY
    RECEIVE name FROM KEYBOARD
END WHILE
SET message TO "Hello " + name
SEND message TO DISPLAY
```

Indent instructions inside an `IF` or loop so their scope is clear.

---

## 6. Pseudocode keywords

| Purpose | Write |
|---|---|
| Input | `RECEIVE choice FROM KEYBOARD` |
| Output | `SEND "Hello" TO DISPLAY` |
| Assignment | `SET total TO 0` |
| Decision | `IF ... THEN ... ELSE ... END IF` |
| Repeat | `WHILE ... END WHILE` or `FOR EACH ... NEXT` |
| Function | `FUNCTION get_dates() ... RETURN start, end` |
| Call a function | `CALL calculate_summary()` |

Include data types and structures when they help explain the design:

```text
SET count (integer) TO 0
SET total_prize (real) TO 0.0
SET athlete_names (list of strings) TO unique athlete names
```

---

## 7. Menu design with validation

Ask for a choice and repeat until it is in the allowed range.

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

The validation loop is an example of **iteration**. The range check is an
example of **selection**.

---

## 8. Select an item from a numbered list

Do not ask whether a name is a string: a name read from a list already is
text. Check that the selected number is within the list.

```text
FUNCTION get_athlete(dataframe)
    SET athlete_names TO unique values from dataframe["Athlete"]
    SEND "Choose an athlete" TO DISPLAY

    FOR EACH name IN athlete_names
        SEND position number and name TO DISPLAY
    NEXT name

    RECEIVE selection (integer) FROM KEYBOARD
    WHILE selection is less than 1 OR
          selection is greater than length of athlete_names
        SEND "Choose a number from the list" TO DISPLAY
        RECEIVE selection (integer) FROM KEYBOARD
    END WHILE

    SET chosen_athlete TO athlete_names[selection - 1]
    RETURN chosen_athlete
END FUNCTION
```

Using a numbered list makes the input easier to validate and avoids spelling
mistakes.

---

## 9. Validate a date range

Check the format and validity of both dates before comparing them. The end
date must not be before the start date.

```text
FUNCTION get_dates()
    RECEIVE start_date (dd/mm/yyyy) FROM KEYBOARD
    RECEIVE end_date (dd/mm/yyyy) FROM KEYBOARD

    WHILE either date is not valid
        SEND "Enter valid dates in dd/mm/yyyy format" TO DISPLAY
        RECEIVE start_date FROM KEYBOARD
        RECEIVE end_date FROM KEYBOARD
    END WHILE

    CONVERT start_date TO a date
    CONVERT end_date TO a date

    WHILE end_date is before start_date
        SEND "End date must not be before start date" TO DISPLAY
        RECEIVE start_date FROM KEYBOARD
        RECEIVE end_date FROM KEYBOARD
        VALIDATE both dates again
        CONVERT both dates TO dates
    END WHILE

    RETURN start_date, end_date
END FUNCTION
```

Do not compare unparsed date strings. Validate and convert them first.

---

## 10. Filter rows and count results

Use inclusive comparisons so results on both dates are included.

```text
FUNCTION count_results(data, selected_name, start_date, end_date)
    SET count (integer) TO 0
    SET total (real) TO 0.0

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
        SEND count and total TO DISPLAY
    END IF
END FUNCTION
```

**Important:** do not `RETURN` the result inside the loop. That would stop
processing after the first matching row. Decide whether there are results only
after every row has been checked.

---

## 11. A complete design sequence

```text
FUNCTION main()
    IMPORT data-handling library
    READ "Task3a_data.csv"
    SET dataframe TO the data
    SET dataframe["Date"] TO dates parsed as dd/mm/yyyy

    SET choice TO get_menu_choice()

    WHILE choice is not 3
        IF choice is 1 THEN
            SET chosen_athlete TO get_athlete(dataframe)
            SET start_date, end_date TO get_dates()
            CALL show_results(dataframe, chosen_athlete,
                              start_date, end_date)
        ELSE IF choice is 2 THEN
            CALL show_summary(dataframe)
        END IF

        SET choice TO get_menu_choice()
    END WHILE

    SEND "Goodbye" TO DISPLAY
END FUNCTION

CALL main()
```

This sequence shows loading, input, validation, processing, output and
iteration. Adapt the menu options and functions to the actual brief.

---

## 12. Explain design decisions

Use technical vocabulary accurately and explain important choices.

Examples:

- “The athlete is selected from a numbered list so the choice can be checked
  against the list length.”
- “The dates are converted before comparison so day/month/year values are
  ordered correctly.”
- “The counter is initialised before the loop so every matching row is
  included.”
- “The no-results message is displayed after the loop so it is only shown
  when no row matched.”

Communication marks come from making the design understandable to technical
and non-technical readers.

---

## 13. Common design mistakes

| Mistake | Better approach |
|---|---|
| Mixing input, processing and output | Separate the stages and name the functions |
| Writing “check it” | State exactly what is checked and what happens if it fails |
| Asking whether a name is a string | Check whether the selection is in the list |
| Using an unchecked list number | Check it is between 1 and the list length |
| Comparing raw date text | Validate and convert dates first |
| Forgetting to initialise a counter | Set it to zero before the loop |
| Returning inside the counting loop | Finish the loop before displaying results |
| Leaving decision arrows unlabelled | Label both `Yes` and `No` branches |
| Using a rectangle for input/output | Use a parallelogram |
| Renaming functions between design and code | Keep names consistent |
| Leaving shapes disconnected | Connect every path from start to end |

---

## 14. Fast revision list

Remember:

1. Start with the whole problem and decompose it into functions.
2. List inputs, processes and outputs.
3. Show sequence, selection and iteration.
4. Validate every user input with a clear loop.
5. Use numbered lists for selectable names or records.
6. Validate and convert dates before comparing them.
7. Initialise counters before loops.
8. Include both date endpoints when the requirement is inclusive.
9. Handle “no results” after processing all rows.
10. Use the same names in pseudocode, flowcharts and Python.

---

## 15. Task 3 design checklist

- [ ] Inputs, processes and outputs are clearly listed.
- [ ] The problem is decomposed into named functions.
- [ ] Function names match the intended Python implementation.
- [ ] Flowchart symbols are used correctly.
- [ ] Every flowchart path is connected.
- [ ] Decision branches are labelled `Yes` and `No`.
- [ ] Sequence, selection and iteration are shown.
- [ ] Validation loops repeat until input is valid.
- [ ] Athlete or person choices come from a numbered, validated list.
- [ ] Dates use `dd/mm/yyyy` and the end is not before the start.
- [ ] Start and end dates are included when required.
- [ ] Counters and totals are initialised before loops.
- [ ] “No results” is handled after the loop.
- [ ] Data types and structures are clear.
- [ ] Important design decisions are justified.
- [ ] The design has a clear beginning and ending.

**Assessment tip:** another developer should be able to implement the
solution from the design without having to guess what a step means.
