from tools.general import load_input_ints

def chain_all_adaptors(sorted_adaptor_list):
    # socket = 0, device = (highest rated adaptor + 3)
    return [0] + sorted_adaptor_list + [sorted_adaptor_list[-1] + 3]

def joltage_differences(adaptor_chain):
    return [a - adaptor_chain[i] for i, a in enumerate(adaptor_chain[1:])]

def count_possible_chains(sorted_adaptor_list):

    # Number of possible chains from the socket to each adaptor
    # Trivial chain to the socket itself
    chains = {0:1}

    # Number of chains to any adaptor is sum of number of chains to each
    # adaptor that can connect to it (i.e. is rated 1-3 jolts lower)
    for a in adaptors:
        chains[a] = sum(chains.get(j, 0) for j in range(a - 3, a))

    # Only the highest rated adaptor can connect directly to the device
    return chains[sorted_adaptor_list[-1]]

adaptors = sorted(load_input_ints("day10.txt"))
jdiffs = joltage_differences(chain_all_adaptors(adaptors))
print(f"Part 1 => {jdiffs.count(1) * jdiffs.count(3)}")
print(f"Part 2 => {count_possible_chains(adaptors)}")
