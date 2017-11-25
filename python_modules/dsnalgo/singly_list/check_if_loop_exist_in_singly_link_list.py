class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class Singly_link(object):
    def __init__(self):
        self.head = None

    def insert_at_last(self, data, point_some_already_present_node=None):
        if self.head is None:   # handle scenario where singly_list is empty
            self.head = Node(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        if point_some_already_present_node is not None:
            temp.next.next = point_some_already_present_node


    def is_loop_present_in_list_using_address_check(self):
        node_address = []
        temp = self.head
        while(temp):
            if id(temp) not in node_address:
                node_address.append(id(temp))
                temp = temp.next
            else:
                return True
        return False

    def is_loop_present_in_list_using_two_pointers_move(self):
        single = self.head
        double = self.head

        while(single and double):
            single = single.next
            double = double.next.next
            if single == double:
                return True
        return False

    def find_length_of_loop(self):
        if not self.is_loop_present_in_list_using_address_check():
            print "No loop exist in the linked singly_list"
            return

        node_address = []
        temp = self.head
        while(temp):
            if id(temp) not in node_address:
                node_address.append(id(temp))
                temp = temp.next
            else:
                address = id(temp)
                break
        temp = self.head
        addd_count = 0
        loop_count = 0
        while addd_count != 2:
            #print temp.data
            if addd_count == 0 and id(temp) == address:
                addd_count = 1
            elif addd_count == 1 and id(temp) != address:
                loop_count = loop_count + 1
            elif addd_count == 1 and id(temp) == address:
                addd_count = 2
                loop_count = loop_count + 1
            temp = temp.next
        return loop_count


            


    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

sl=Singly_link()
sl.insert_at_last(10)
sl.insert_at_last(20)
sl.insert_at_last(30)
sl.insert_at_last(40)
sl.insert_at_last(50)
sl.insert_at_last(60, point_some_already_present_node=sl.head)
#sl.print_list()
#print sl.is_loop_present_in_list_using_address_check()
#print sl.is_loop_present_in_list_using_two_pointers_move()
print "Loop count is %s" % sl.find_length_of_loop()

