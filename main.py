import unittest


def mat_to_list(adj_mat):
    adj_list = []

    for adj_nodes in adj_mat:
        adj_list.append([])

        for adj_node, value in enumerate(adj_nodes):
            if value == 1:
                adj_list[len(adj_list) - 1].append(adj_node)

    return adj_list


def reachable(adj_list, start_node):
    node = start_node
    reachable_nodes = set()

    for i, adj_node in enumerate(adj_list[node]):
        if adj_node == "-":
            continue

        reachable_nodes.add(adj_node)

        modified_adj_list = adj_list.copy()

        modified_nodes_list = modified_adj_list[node].copy()
        modified_nodes_list[i] = "-"

        modified_adj_list[node] = modified_nodes_list

        nodes = reachable(modified_adj_list, adj_node)

        for n in nodes:
            reachable_nodes.add(n)

    return reachable_nodes


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.adj_list = [[1, 3], [2], [0], [4], [3], []]

    def test_mat_to_list(self):
        adj_matrix = [[0, 1, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        result = mat_to_list(adj_matrix)
        expected = self.adj_list

        self.assertEqual(result, expected)
        print("test_mat_to_list is passed..")

    def test_reachable(self):
        start_node = 0
        result = reachable(self.adj_list, start_node)
        expected = {0, 1, 2, 3, 4}

        self.assertEqual(result, expected)

        start_node = 3
        result = reachable(self.adj_list, start_node)
        expected = {3, 4}

        self.assertEqual(result, expected)
        print("test_reachable is passed..")


if __name__ == '__main__':
    unittest.main()
