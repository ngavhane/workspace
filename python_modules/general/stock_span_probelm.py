"""
  The stock span probelm
  For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
  then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
"""
def give_span(stock_array):
    temp = []
    for t in  stock_array:
        temp.append(1)
    for index, ele in enumerate(stock_array):
        if index == 0:
            continue
        j = index - 1
        while(j > -1 and stock_array[index]> stock_array[j]):
            print "in while loop"
            temp[index] = temp[index] + 1
            j = j-1
    return temp



if __name__ == "__main__":
    res = give_span([100, 80, 60, 70, 60, 75, 85])
    print res
