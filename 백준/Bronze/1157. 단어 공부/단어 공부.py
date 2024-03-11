ans = input().upper()
freq = {}
max_freq = 0
max_char = []

for i in ans:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

    if freq[i] > max_freq:
        max_freq = freq[i]
        max_char = [i]
    elif freq[i] == max_freq:
        max_char.append(i)

if len(set(max_char)) == 1:
    print(max_char[0])
else:
    print("?")