
def binary_search(list1, elememt):
    if len(list1) ==1:
        if elememt == list1[0]:
            return True
        else:
            return False
    median = len(list1)/2
    if elememt == list1[median]:
        return True
    elif(elememt > list1[median]):
        binary_search(list1[median+1:], elememt)
    else:
        binary_search(list1[:median-1], elememt)
        

if __name__ == "__main__":
    ele = [1, 2, 3]
    ele.sort()
    print ele
    elememt = raw_input("enter number that you want to search")
    print binary_search(ele, int(elememt))
