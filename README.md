# Password Validator & Strength Checker

Python scripts that validate passwords against security requirements and score their strength, built while learning core Python fundamentals.

## Files

### `Password_Validator.py`
Validates a password against a set of requirements, re-prompting the user until all are met.

**What it checks:**
- Minimum length (12 characters)
- At least one uppercase letter
- At least one digit
- At least one special symbol (!, @, #, $, %, &)

### `Password_Strength.py`
Builds on the validator above by scoring the strength of a password once it passes validation, rating it Weak, Medium, or Strong.

**How scoring works:**
- +1 point for each character over the 12-character minimum
- +1 point for each uppercase letter
- +1 point for each digit
- +1 point for each symbol
- Score of 3 → Weak, 4-5 → Medium, 6+ → Strong

## Concepts used
Variables, user input, type casting, if/elif/else statements, while loops, for loops, and string methods.

## What I learned
While building the validator, I ran into a bug where my validation logic would pass a check for one requirement, but wouldn't re-verify that same requirement after a later failed check triggered a new password entry. Fixing it taught me a lot about how loop state needs to be reset and re-evaluated on each pass.

While building the strength checker, I ran into a couple of related bugs:
- Using `break` inside a counting loop stopped the count at the first match instead of counting every occurrence — `break` made sense for the validator's pass/fail checks, but not for counting totals.
- My score range conditions initially had a boundary error where a bare-minimum password could be mislabeled — fixed by tracing through the actual minimum guaranteed score and adjusting the ranges to match.

## Next steps
Considering adding a maximum attempt limit, or expanding the scoring system to account for common/weak password patterns.
