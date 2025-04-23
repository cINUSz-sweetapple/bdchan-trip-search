# bdchan-trip-search
A fast, multi-process brute-force tool to find bdchan-style tripcodes that visually resemble any desired word or pattern. It uses SHA-256 + Base64 (first 6 chars) to generate tripcodes and compares them with a customizable wordlist using fuzzy matching (via RapidFuzz).
