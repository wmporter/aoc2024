left = []
right = []
with open('input') as f:
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()
total = 0
for i in range(len(left)):
    total += abs(left[i]-right[i])

print(total)

counts = {}
total = 0
for r in right:
    if r in counts:
        counts[r] += 1
    else:
        counts[r] = 1
for l in left:
    if l in counts:
        total += l * counts[l]

print(total)
