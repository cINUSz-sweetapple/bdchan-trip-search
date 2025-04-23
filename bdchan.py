import hashlib
import base64
import random
import string
from rapidfuzz import fuzz
import multiprocessing

# Customize your prefix here
prefix = "abcdefghij" #Type your own suffix | NOT MORE THAN 19 CHARS
output_file = "matches.txt"
suffix_length = 4  # You can increase this if needed
#TOTAL CHAR LIMIT SHOULDNT CROSS MORE THAN 16

# List of target patterns to match against
# Add your own things.

target_words = [
    'admin', 'root', 'ghost',
    'hacker', 'shadow', 'alpha',
    'omega', 'null', 'neo', 'anon',
    'chaos', 'code', 'king', 'queen',
    'test', 'demo'
]

def generate_candidate(length=suffix_length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def check_match(trip):
    for word in target_words:
        score = fuzz.ratio(trip, word)
        if score >= 80:
            return word, score
    return None, None

def worker(process_id):
    while True:
        suffix = generate_candidate()
        full_input = prefix + suffix
        h = hashlib.sha256(full_input.encode("utf-8")).digest()
        trip = base64.b64encode(h).decode("utf-8")[:6]

        match_word, score = check_match(trip)
        if match_word:
            line = f"{trip} ≈ {match_word} ({score}%) ← {full_input}\n"
            with open(output_file, "a") as f:
                f.write(line)
            print(line.strip())

if __name__ == "__main__":
    print("Starting Tripcode Pattern Hunter...")
    processes = []
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
