
def binary_search(list1, find):
    i=0
    j=len(list1)-1
    while(len(list1)!=1):
        print list1
        median = len(list1)/2
        print median
        if (list1[median]==find):
           return True
        elif(find > list1[median]):
            list1=list1[median:]
        else:
            list1=list1[:median]
    return False
if __name__ == "__main__":
    count = int(raw_input("Enter number of elements :"))
    inputs = []
    for i in range(count):
        x=int(raw_input("enter %s the element:" % i))
        inputs.append(x)
    inputs.sort()
    elememt = raw_input("enter number that you want to search:")
    resp =  binary_search(list1=inputs, find=int(elememt))
    print resp
