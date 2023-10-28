def main():
    with open("./Data/0107_network.txt") as f:
        graph = f.read().splitlines()
    graph = [line.split(',') for line in graph]

    def _convert(item):
        if item == "-":
            return 0
        else:
            return int(item)
    graph = [[_convert(item) for item in line] for line in graph]

    nb_nodes = len(graph)
    max_weight = max([max(line) for line in graph])
    total_weights = sum([sum(line) for line in graph]) // 2
    selected_nodes = {0}
    non_selected_nodes = set(range(1, nb_nodes))

    non_removed_total = 0
    while len(selected_nodes) < nb_nodes:
        least_weight = max_weight + 1
        best_edge = 0, 0
        for node1 in selected_nodes:
            for node2 in non_selected_nodes:
                if 0 < graph[node1][node2] < least_weight:
                    least_weight = graph[node1][node2]
                    best_edge = node1, node2
        selected_nodes.add(best_edge[1])
        non_removed_total += least_weight
        non_selected_nodes.remove(best_edge[1])

    return total_weights - non_removed_total
