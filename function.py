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

    cycles = []
    for node in graph:
        visited = set()
        dfs(node, node, visited, [])
    return cycles


# 示例输入
# graph = {2: 4, 3: 9, 4: 4, 5: 8, 6: 2, 7: 5, 8: 11, 9: 1, 10: 10, 11: 5}
# cycles = find_cycles(graph)
# print(cycles)

def reverse_dict(original_dict):
    reversed_dict = {}
    for key, value in original_dict.items():
        if value not in reversed_dict:
            reversed_dict[value] = [key]
        else:
            reversed_dict[value].append(key)
    return reversed_dict


# 测试样例
# original_dict = {2: 7, 3: 11, 4: 10, 5: 10, 7: 2, 9: 5, 10: 10, 11: 5}
# reversed_dict = reverse_dict(original_dict)
# print(reversed_dict)

def group_by_list_length(input_dict):
    grouped_dict = {}
    for key, value in input_dict.items():
        list_length = len(value)
        if list_length not in grouped_dict:
            grouped_dict[list_length] = {key: value}
        else:
            grouped_dict[list_length][key] = value
    return grouped_dict


# 测试样例
input_dict = {1: [4], 3: [2]}
grouped_dict = group_by_list_length(input_dict)
print(grouped_dict)
