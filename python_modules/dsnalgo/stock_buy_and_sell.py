"""

The cost of a stock on each day is given in an array, find the max profit
that you can make by buying and selling in those days.
For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0,
selling on day 3. Again buy on day 4 and sell on day 6.
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

"""


def get_buy_sell_sequence(seq):
    total= []
    for index1, item in enumerate(seq):
        for index2, item2 in enumerate(seq):
            if index1 != index2:
                










get_buy_sell_sequence([100, 180, 260, 310, 40, 535, 695])
