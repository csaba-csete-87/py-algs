class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)


def dijkstra(start_node, end_node):
    if start_node.value == end_node.value:
        return 0
    distances = {}
    stack = [start_node]
    distances[start_node.value] = 0
    visited = []
    while len(stack) > 0:
        crt = stack.pop(0)
        for edge in crt.edges:
            node_val = edge.node.value
            if node_val in visited:
                continue
            stack.append(edge.node)

            dist = distances[crt.value] + edge.distance

            if node_val not in distances:
                distances[node_val] = dist
            else:
                crt_dist = distances[node_val]
                if dist < crt_dist:
                    distances[node_val] = dist
        visited.append(crt.value)

    return distances[end_node.value]


node_1 = node_u
node_2 = node_y

print('Shortest Distance from {} to {} is {}'.format(node_1.value, node_2.value, dijkstra(node_1, node_2)))
