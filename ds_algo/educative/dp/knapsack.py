from typing import List

def knap_sack(profits, profits_length, weights, capacity):

    weights_length = profits_length
    # Basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]

    # Building the lookup table in bottom up manner
    for i in range(profits_length+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            # can add an item to the knapsack
            elif weights[i-1] <= j:
                lookup_table[i][j] = max(profits[i-1]+lookup_table[i-1][j-weights[i-1]],lookup_table[i-1][j])
            # cannot add an item
            else:
                lookup_table[i][j] = lookup_table[i-1][j]

    print(lookup_table)

    return lookup_table[profits_length][capacity]



def knap_sack_recurvise2(lookup_table:List[int],profits:List[int], profits_length:int, weights:List[int], capacity:int, current_index:int) -> int:
    # base case:
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0
    # use lookup instead
    if lookup_table[current_index][capacity] != 0:
        return lookup_table[current_index][capacity]

    # recursive call after choosing the element at the current_index
    # with the new item added
    # if the weight of the element at current_index exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recurvise2(lookup_table, profits, profits_length, weights,capacity - weights[current_index], current_index + 1)

    # wihth out the item recursive call after excluding the element at the current_index
    profit2 = knap_sack_recurvise2(lookup_table, profits, profits_length, weights, capacity, current_index + 1)

    lookup_table[current_index][capacity] = max(profit1, profit2)
    return lookup_table[current_index][capacity]

def knap_sack_recursive(profits, profits_length, weights, capacity, current_index):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each item
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :param current_index: Current index of the weights
    :return: Maximum value that can be put in a knapsack
    """

    # Base Case
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    # If weight of the nth item is more than Knapsack, then
    # this item cannot be included in the optimal solution
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(profits, profits_length, weights,
                                                     capacity - weights[current_index], current_index + 1)

    profit2 = knap_sack_recursive(profits, profits_length, weights, capacity, current_index + 1)

    return max(profit1, profit2)


def main(profits, profits_length, weights, capacity):
    #return knap_sack_recursive(profits, profits_length, weights, capacity, 0)
    #lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
    #return knap_sack_recurvise2(lookup_table, profits, profits_length, weights, capacity, 0)
    return knap_sack(profits, profits_length, weights, capacity)

# main gaurd
if __name__ == "__main__":

    assert main([60, 100, 120], 3, [10, 20, 30], 50) == 220
    assert main([60, 100, 120], 3, [10, 20, 30], 30) == 160
    assert main([60, 100, 120], 3, [10, 20, 30], 10) == 60



