class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Singlylink(object):
    def __init__(self, data):
        self.head = Node(data)

    def insert_at_last(self, data):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def insert_after_node(self, data, after_node):
        temp = self.head
        while temp.data != after_node:
            temp = temp.next
        xyz = temp
        pqr = temp.next
        xyz.next = Node(data)
        xyz.next.next = pqr

    def print_list(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def merge_two_sorted_list(self, first_head, second_head):
        temp1 = first_head
        temp2 = second_head
        third_head = None
        while temp1 or temp2:
            if temp1 is None:
                print "%s is getting pushed" % temp2.data
                xyz = third_head
                if third_head is None:
                    third_head = Node(temp2.data)
                else:
                    while xyz.next:
                        xyz = xyz.next
                    xyz.next = Node(temp2.data)
                temp2 = temp2.next
            elif temp2 is None:
                print "%s is getting pushed" % temp1.data
                xyz = third_head
                if third_head is None:
                    third_head = Node(temp1.data)
                else:
                    while xyz.next:
                        xyz = xyz.next
                    xyz.next = Node(temp1.data)
                temp1 = temp1.next
            elif temp1.data < temp2.data:
                print "%s is getting pushed" % temp1.data
                if third_head is None:
                    third_head = Node(temp1.data)
                else:
                    xyz = third_head
                    while xyz.next:
                        xyz = xyz.next
                    xyz.next = Node(temp1.data)
                temp1 = temp1.next
            else:
                print "%s is getting pushed" % temp2.data
                if third_head is None:
                    third_head = Node(temp2.data)
                else:
                    xyz = third_head
                    while xyz.next:
                        xyz = xyz.next
                    xyz.next = Node(temp2.data)
                temp2 = temp2.next
        print "Printing content of the merged list"
        temp = third_head
        while temp:
            print temp.data
            temp = temp.next


sl1 = Singlylink(10)
sl1.insert_at_last(20)
sl1.insert_at_last(30)
sl1.insert_at_last(40)
sl1.print_list()
print "***"

sl2 = Singlylink(-9)
sl2.insert_at_last(4)
sl2.insert_at_last(35)
sl2.insert_at_last(45)
sl2.print_list()
print "***"

sl1.merge_two_sorted_list(sl1.head, None)




