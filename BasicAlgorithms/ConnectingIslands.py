import heapq

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    prices = list()
    islands = set()
    for config in bridge_config:
        heapq.heappush(prices, (config[2], (config[0], config[1])))
        islands.add(config[0])
        islands.add(config[1])
    cost = 0
    while len(islands) > 0 or len(prices) > 0:
        priceConfig = heapq.heappop(prices)
        price = priceConfig[0]
        i_1 = priceConfig[1][0]
        i_2 = priceConfig[1][1]

        cost += price

        if i_1 in islands:
            islands.remove(i_1)
        if i_2 in islands:
            islands.remove(i_2)

    print(cost)
    return cost

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)