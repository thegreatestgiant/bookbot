# bookbot

A small Python script that reads a novel and prints word and letter-frequency counts.

This was my first **Boot.dev** project, built for the
[Build a Bookbot in Python](https://www.boot.dev/courses/build-bookbot-python) course.

## What was provided vs. what I wrote

| | |
|---|---|
| Provided by Boot.dev | Course lessons and project spec, the CLI test harness, the `books/` novel files (gitignored), and a one-line README starter. |
| Written by me | `main.py` (31 lines): file loading, word count, letter-frequency count, and report formatting; this README; Git setup. |
| Not provided | There was no starter implementation. The guided project asks you to write the program from scratch. |

## Run

The course reads `books/frankenstien.txt` (the filename is misspelled in the code).
Download a plain-text novel to that path, then:

```bash
python3 main.py
```

## Limitations

- Hardcoded path and a misspelled filename.
- No argument parsing, tests, or error handling.
- This is a first learning project, not a portfolio piece.
