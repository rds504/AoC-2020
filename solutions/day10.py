from tools.general import load_input_ints

adaptors = sorted(load_input_ints("day10.txt"))

chain = [0] + adaptors + [adaptors[-1] + 3]
diff1, diff3 = 0, 0

for i, a in enumerate(chain[1:]):
    diff = a - chain[i]
    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

print(f"Part 1 => {diff1 * diff3}")

# Number of possible paths from the socket to each adaptor
# Trivial path to the socket itself
paths = {0:1}

# Number of paths to any adaptor is sum of number of paths to each adaptors that can connect to it
for i in adaptors:
    n_paths = 0
    for j in range(i - 3, i):
        n_paths += paths.get(j, 0)
    paths[i] = n_paths

# Only the highest rated adaptor can connect to the device
print(f"Part 2 => {paths[adaptors[-1]]}")
