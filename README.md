# bdchan-trip-searcher
A fast, multi-process brute-force tool to find bdchan-style tripcodes that visually resemble any desired word or pattern. It uses SHA-256 + Base64 (first 6 chars) to generate tripcodes and compares them with a customizable wordlist using fuzzy matching (via RapidFuzz).

A fast, multi-core Python tool to brute-force `bdchan`-style tripcodes and find ones that resemble custom words using fuzzy matching.

Tripcodes are generated using the first 6 characters of a SHA-256 hash encoded in Base64. This script compares them to target patterns (like `"admin"`, `"ghost"`, `"null"`, etc.) and prints high-similarity matches.

---

## Features

- Generates tripcodes from SHA-256 + Base64
- Fuzzy matching with customizable similarity threshold
- Uses all CPU cores via multiprocessing
- Fully customizable: prefix, suffix length, target words
- Saves matching results in real-time to `matches.txt`

---

## Requirements

**Python version:** 3.6 or higher

**Python packages:**

- `rapidfuzz`

You can install all dependencies by running:

```bash
pip install -r requirements.txt
