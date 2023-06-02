class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next

    def prepend(self,data):
        new_node = Node(data)
        if self.head ==None:
            self.head=new_node
            return 
        temp = self.head
        self.head = new_node
        new_node.next = temp

    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("previous node does not exist")
            return
        
        new_node =Node()

        temp = prev_node.next
        prev_node.next = new_node
        new_node.next = temp

    def del_by_pos(self,pos):
        if self.head:
            cur_node =self.head
            if pos==0:
                self.head = cur_node.next
                cur_node = None
                return
            
            prev = None
            count = 0
            while cur_node and count!=pos:
                prev = cur_node
                cur_node = cur_node.next
                count+=1

            if cur_node is None:
                return
            
            prev.next = cur_node.next
            cur_node = None

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

