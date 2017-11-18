class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def delete_by_value(self, value):
        all_elemt = self.get_all_list_elements()
        if all_elemt.count(value) ==0:
            raise Exception("No such element exist in the list")
        if all_elemt.count(value) > 1:
            raise Exception("More than one such element exist in the list")

        # if the element that you want to delete is the first one.
        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        temp_succ = None
        while temp.data != value:
            temp_succ=temp
            temp = temp.next
        temp_succ.next = temp.next

    def delete_by_index(self, index):
        # if the element that you want to delete is the first one.
        if index == 1:
            self.head = self.head.next
            return
        count = 1
        temp = self.head
        temp_succ = None
        while count != index:
            temp_succ=temp
            temp = temp.next
            count = count + 1
        temp_succ.next = temp.next

    def get_all_list_elements(self):
        all_ele = []
        temp = self.head
        while(temp):
            all_ele.append(temp.data)
            temp = temp.next
        return all_ele

    def print_li(self):
        temp = self.head
        while(temp):
            print temp.data
            temp= temp.next
s=SList()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)
s.print_li()
s.delete_by_index(6)
#s.delete_by_value(10)
print "****"
s.print_li()


