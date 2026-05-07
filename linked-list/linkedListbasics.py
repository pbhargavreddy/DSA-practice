from typing import Optional
class Node():
    def __init__(self,data,next = None):
        self.val = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head : Node | None =None
        self.last : Node | None = None
        pass

    def createNode(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.last = node
        elif self.last:
            self.last.next = node
            self.last = self.last.next

    def createNodesInBulk(self):
        inpud_list = list(map(int , input().split()))
        for val in inpud_list:
            self.createNode(val)
    

    def viewLinkedList(self,head :Node | None = None):
        if head == None:
            temp = self.head
        else:
            temp = head
        if not temp:
            print("list is empty")
            return 
        while temp:
            print(temp.val , end = '-> ' if temp.next else '\n')
            temp = temp.next


    def reverseUsingStack(self):
        temp = self.head
        stack = []
        while temp :
            stack.append(temp)
            temp = temp.next
        new_head = stack.pop()
        new_last = new_head
        while stack:
            new_last.next = stack.pop()
            new_last = new_last.next

        new_last.next = None

        self.viewLinkedList(new_head)
    
    
    def reverseInPlace(self):
        self.last = self.head
        prev = None
        curr = self.head

        while curr :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        
        # self.viewLinkedList()
            
if __name__ == "__main__":
    ll = LinkedList()
    ll.createNode(10)
    ll.createNodesInBulk()
    ll.reverseInPlace()
    ll.viewLinkedList()

