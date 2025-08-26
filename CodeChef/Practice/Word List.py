N = int(input())
words = set()

for _ in range(N):
    line = input().strip()
    # Replace any non-alphabetic character with a space and convert to lowercase
    processed = ''.join(ch.lower() if ch.isalpha() else ' ' for ch in line)
    for token in processed.split():
        words.add(token)

sorted_words = sorted(words)
print(len(sorted_words))
for w in sorted_words:
    print(w)