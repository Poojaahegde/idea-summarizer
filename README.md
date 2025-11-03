# Idea Summarizer (No APIs)

A tiny CLI tool that reduces any block of text into the 3 most representative sentences using simple word-frequency scoring (no external libraries).

## Why it's useful (APM angle)
- Demonstrates pragmatic AI thinking with constraints (no internet, no APIs).
- Shows how you'd ship a simple offline summarizer for notes, interviews, or PRDs.

## How to run
```bash
python summarizer.py "path/to/notes.txt"
# or: echo "paste text here" | python summarizer.py
```

## Files
- `summarizer.py` — main script
- `sample.txt` — sample input
- `README.md` — you are here
