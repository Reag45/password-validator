# Password Validator
A Python script that validates passwords against a set of security requirements, built while learning core Python fundamentals.

## What it checks
- Minimum length (12 characters)
- At least one uppercase letter
- At least one digit
- At least one special symbol (!, @, #, $, %, &)

## Concepts used
Variables, user input, type casting, if/elif statements, while loops, for loops, and string methods.

## What I learned
While building this, I ran into a bug where my validation logic would pass a check for one requirement, but would not re-verify that same requirement after a later failed check triggered a new password entry. Fixing it taught me a lot about how loop state needs to be reset and re-evaluated on each pass.

## Next steps
Adding an actual password strength scoring system (weak/medium/strong) on top of the current validation.
