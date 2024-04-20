class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class MyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def addAtHead(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head =  new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size +=1
        
    def addAtTail(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head =  new_node
            self.tail = new_node
        else:
            new_tail = self.tail
            new_tail.next = new_node
            self.tail = new_node
        self.size +=1        
    
    def insertAtIndex(self , value , index):
        if index < 0 and index > self.size:
            return 
                
        new_node = Node(value)
        cur = self.head
        
        if index == 0:
            self.addAtHead(value)
        elif index == self.size:
            self.addAtTail(value)
        else:
            position = 0
            
            while position != index-1:
                cur = cur.next
                position +=1
    
            new_node.next = cur.next
            cur.next = new_node
            
            self.size +=1         
            
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
                
    def removeFirstNode(self):
        if self.head is None:
            return
        self.head = self.head.next
        
        self.size -=1
    
    def removeLastNode(self):
        if self.head is None:
            return
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None
        
        self.size -=1  
    
    def removeIndexNode(self ,  index):
        if index < 0 and index > self.size:
            return
        elif index == 0:
            self.removeFirstNode()
        elif index == self.size:
            self.removeLastNode()
        else:
            cur = self.head
            position = 0
            while position != index-1 :
                cur =cur.next
                position +=1
            cur.next = cur.next.next
            self.size -=1        
            
    def printLL(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next
            
obj = MyLinkedList()
print("Linked List Operation:")

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
            obj.insertAtIndex(val , ind)        
    elif choice == 4:
        obj.removeFirstNode()
    elif choice == 5:
        obj.removeLastNode()
    elif choice == 6:
        ind = int(input("Which Index Node Element You Want To Delete:"))
        obj.removeIndexNode(ind)
    elif choice == 7:
        obj.printLL()
    elif choice == 8:
        ind = int(input("Enter The index You want to Update "))
        val = input("Enter The The Value:")
        obj.updateNode(val , ind)  
    elif choice == 9:
        test = 2    
    else:
        print("Invalid Choice ")
    
    
    
    

