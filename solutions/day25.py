from tools.general import load_input_ints

def transform(subject, loop_size, modulus = 20201227):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % modulus
    return value

def brute_force_loop_size(key, subject = 7, modulus = 20201227):

    loop_size = 0
    xformed   = 1

    while True:
        loop_size += 1
        xformed = (xformed * subject) % modulus
        if xformed == key:
            return loop_size

def ascii_art_star():
    print(r"   __/\__ ")
    print(r"   \    / ")
    print(r"   /_  _\ ")
    print(r"     \/   ")

pub_key1, pub_key2 = load_input_ints("day25.txt")

print(f"Part 1 => {transform(pub_key2, brute_force_loop_size(pub_key1))}")
print("Part 2 => free :)")
ascii_art_star()
