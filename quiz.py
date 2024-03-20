# COMP9021 24T1
# Quiz 1 *** Due Thursday Week 3 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Sunday Week 3 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}


# INSERT YOUR CODE HERE


def find_cycles(graph):
    def dfs(node, start, visited, path):
        visited.add(node)
        path.append(node)
        if graph[node] == start:
            cycle = sorted(path[:])
            if cycle not in cycles:
                cycles.append(cycle)
        else:
            neighbor = graph.get(node)
            if neighbor in graph:
                if neighbor not in visited:
                    dfs(neighbor, start, visited, path)
        path.pop()
        visited.remove(node)

    for node in graph:
        visited = set()
        dfs(node, node, visited, [])
    return cycles


# def is_cycle_equivalent(new_cycle, existing_cycles):
#     for cycle in existing_cycles:
#         if len(new_cycle) != len(cycle):
#             continue
#         # conpare two String
#         cycle_str = ''.join(map(str, cycle))
#         new_cycle_str = ''.join(map(str, new_cycle))
#         if any(new_cycle_str == cycle_str[i:] + cycle_str[:i] for i in range(len(cycle_str))):
#             return True
#     return False


def reverse_dict(original_dict):
    reversed_dict = {}
    for key, value in original_dict.items():
        if value not in reversed_dict:
            reversed_dict[value] = [key]
        else:
            reversed_dict[value].append(key)
    return reversed_dict


def group_by_list_length(input_dict):
    grouped_dict = {}
    for key, value in input_dict.items():
        list_length = len(value)
        if list_length not in grouped_dict:
            grouped_dict[list_length] = {key: value}
        else:
            grouped_dict[list_length][key] = value
    return grouped_dict


cycles = find_cycles(mapping)
reversed_dict_per_length = group_by_list_length(reverse_dict(mapping))

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
