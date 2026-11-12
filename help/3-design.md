# Task 3 · Designing a solution

**18 marks:** Decomposition 9 · Logic and conventions 6 · Communication 3

## 1. The five shapes

```mermaid
flowchart LR
    T([Start / End]) --> IO[/Input or output/] --> P[Process] --> D{Decision?} -- yes --> S[[Sub-process]]
    D -- no --> T2([End])
```

| Shape | Use for |
|---|---|
| Rounded (terminator) | Start and End, once each |
| **Parallelogram** | **Every** `input()` and every `print` |
| Rectangle | Set, add, calculate |
| Diamond | A question, with **both arrows labelled** yes / no |
| Double-sided box | Calling a function drawn elsewhere |

## 2. Decompose top-down

```mermaid
flowchart TD
    ROOT[Results program] --> IN[Inputs] & PR[Processes] & OUT[Outputs]
    IN --> I1[Menu choice 1–4] & I2[Person from a numbered list] & I3[Start and end date]
    PR --> P1[Load and clean CSV] & P2[Filter by person + dates] & P3[Count, total, average]
    OUT --> O1[Labelled table] & O2[Graph with title] & O3["'No results' message"]
```

Each box becomes one sub-process in your flowchart and one function in your code. Use the same names in both.

## 3. Validation loop

```mermaid
flowchart TD
    A[/Input menu choice/] --> B{Number 1 to 4?}
    B -- no --> C[/"'Enter 1 to 4'"/] --> A
    B -- yes --> D([Return choice])
```

```text
RECEIVE choice FROM KEYBOARD
WHILE choice NOT IN 1..4
    SEND "Enter 1 to 4" TO DISPLAY
    RECEIVE choice FROM KEYBOARD
END WHILE
```

Dates: check the format (dd/mm/yyyy) → check end ≥ start → then convert.

## 4. Counting loop: decide after the loop

```mermaid
flowchart TD
    S[All counts = 0] --> M{More rows?}
    M -- yes --> Q{Right person AND<br/>date in range?}
    Q -- no --> M
    Q -- yes --> ADD[Add 1 to that place<br/>add prize money] --> M
    M -- no --> F{Any found?}
    F -- yes --> OUT[/Show counts and £/]
    F -- no --> NO[/"'No results'"/]
```

```text
SET count TO 0
FOR EACH row IN data
    IF row.Name = name AND row.Date >= start AND row.Date <= end THEN
        SET count TO count + 1
    END IF
NEXT row
IF count = 0 THEN
    SEND "No results" TO DISPLAY
ELSE
    SEND count TO DISPLAY
END IF
```

## 5. Pseudocode keywords

| For | Write |
|---|---|
| Input | `RECEIVE x FROM KEYBOARD` |
| Output | `SEND x TO DISPLAY` |
| Assign | `SET total TO total + prize` |
| Decide | `IF … THEN … ELSE … END IF` |
| Loop | `FOR EACH … NEXT` · `WHILE … END WHILE` |
| Function | `FUNCTION get_dates() … RETURN start, end` |

## Never

- ❌ `RETURN` inside the loop (it stops at the first non-match)
- ❌ "Is the name a string?" (always yes; check it's **in the list** instead)
- ❌ Unlabelled decision arrows
- ❌ Inputs drawn as rectangles
- ❌ Floating, unconnected shapes
