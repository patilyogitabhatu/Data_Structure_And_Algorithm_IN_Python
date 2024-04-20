class Node():
    def __init__(self , value):
        self.value = value
        self.prev = None
        self.next = None
class MyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addAtHead(self , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
        self.size += 1
        
    def addAtTail(self , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
        self.size +=1   
        
    def addAtIndex(self , val , index):
        if index < 0 and index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size-1:
            self.addAtTail(val) 
        else:
            new_node = Node(val)
            position = 0
            cur = self.head
            while position != index-1:
                cur = cur.next
                position +=1
            cur.next.pre = new_node
            new_node.next = cur.next 
            cur.next = new_node
            new_node.prev = cur
            
            self.size +=1                  
        
    def deleteAtHead(self):
        if self.head is None :
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            return
            
        cur = self.head.next
        cur.prev = None
        self.head = cur
        self.size -=1
        
    def deleteAtTail(self):
        if self.head is None :
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            return
        
        cur = self.tail.prev
        cur.next = None
        self.tail = cur
        
        self.size -=1
    
    def deleteAtIndex(self , index):
        if index < 0 and index > self.size:
            return
        if index == 0:
            self.deleteAtHead()
        elif index == self.size-1:
            self.deleteAtTail() 
        else:
            cur = self.head
            positon = 0
            
            while positon != index-1:
                cur = cur.next
                positon +=1
                
            ind_node = cur.next
            cur.next = ind_node.next
            ind_node.prev = ind_node.prev
            
            self.size -=1

    def updateNode(self , val , index):
        if index < 0 and index > self.size:
            print("Index Not Found")
        else:
            cur = self.head
            position = 0
            
            while position != index:
                cur = cur.next
                position +=1
            
            cur.value = val
                    
    def printList(self):
        if self.head is None :
            return
        cur = self.head
        position = 0
        while position < self.size:
            print(cur.value)
            cur = cur.next
            position +=1
        
obj = MyLinkedList()
print(" Doubly Linked List Operation:")

linked_list_ele = int(input("How Many Elements Do you Want To add To the Linked List: "))
print(linked_list_ele)


for i in range(0 , linked_list_ele):
    ele = input("Enter {} Element: ".format(i))
    obj.addAtTail(ele)


test = 1
while(test == 1):
    choice = int(input("Operations : \n 1. Add Element At Head \n 2. Add Element At Tail \n 3. Add Element At Perticular Index \n 4. Delete The Head Node \n 5. Delete The Last Node \n 6. Delete The Element At Perticular Index \n 7. Print All The Linked List Elements \n 8. Update The Node Element \n 9. Exit \n Enter Your Choice:  "))

    if choice == 1 or choice ==2 or choice == 3:
        val = input("Enter The Element You want To Add: ")
        if choice == 1:
            obj.addAtHead(val)
        elif choice == 2:
            obj.addAtTail(val)
        elif choice == 3:
            ind = int(input("At Which Index: "))
            obj.addAtIndex(val , ind)        
    elif choice == 4:
        obj.deleteAtHead()
    elif choice == 5:
        obj.deleteAtTail()
    elif choice == 6:
        ind = int(input("Which Index Node Element You Want To Delete:"))
        obj.deleteAtIndex(ind)
    elif choice == 7:
        obj.printList()
    elif choice == 8:
        ind = int(input("Enter The index You want to Update "))
        val = input("Enter The The Value:")
        obj.updateNode(val , ind)  
    elif choice == 9:
        test = 2    
    else:
        print("Invalid Choice ")
                 
            