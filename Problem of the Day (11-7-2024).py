#Node calss
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    #insert a new node at the end of the linked list
    def insert(self, data):
        new_node = Node(data)

        #Insert in an empty list
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while (current.next):
            current = current.next

        current.next = new_node

    #Function to perform the addition of two Linked Lists
    def addTwoLinkedList(self, llist1, llist2):
        currentLL1 = llist1.head
        currentLL2 = llist2.head
        carry = 0
        #Iterate through the two linked lists
        while (currentLL1 is not None or currentLL2 is not None):
            data = 0

            #Check if the first linked list is empty and deal with that
            if currentLL1 is None:
                data = (currentLL2.data + carry) % 10
                carry = (currentLL2.data + carry) // 10
                self.insert(data)
                currentLL2 = currentLL2.next
                continue
            
            #Check if the second linked list is empty and deal with that
            if currentLL2 is None:
                data = (currentLL1.data + carry) % 10
                carry = (currentLL1.data + carry) // 10
                self.insert(data)
                currentLL1 = currentLL1.next
                continue

            #Do the addition operation when both linked lists still have data
            data = ((currentLL1.data + currentLL2.data) % 10) + carry
            carry = (currentLL1.data + currentLL2.data)//10

            self.insert(data)

            currentLL1 = currentLL1.next
            currentLL2 = currentLL2.next

        #Add the carry to the result at the end
        if carry != 0:
            self.insert(carry)

    #Print the contents of the linked list
    def printLinkedList(self):
        current = self.head
        string = ""
        while current.next:
            string = string + str(current.data) + ' -> '
            current = current.next
        string = string + str(current.data)
        return string


#main function
def main():
    #Ask the user to enter the numbers
    list1 = input('Enter the numbers of the first list(sperated by SPACES): ')
    list2 = input('Enter the numbers of the second list(sperated by SPACES): ')

    list1 = list1.strip().split(' ')
    list2 = list2.strip().split(' ')

    #Validate user input
    for i in list1:
        if not i.isdigit():
            print ('Invalid input (must be numbers)...!')
            return

    for j in list2:
        if not j.isdigit():
            print ('Invalid input (must be numbers)...!')
            return

    #Convert the input into integers
    list1 = list(map(int, list1))
    list2 = list(map(int, list2))

    #Create linked lists for each input list
    linkedList1 = makeLinkedList(list1)
    linkedList2 = makeLinkedList(list2)

    #Create new linked list to hold the result values of the addition
    additionLinkedList = addition(linkedList1, linkedList2)
    
    #Print the linked list of the resutl
    print ("The addition linked list is:", additionLinkedList.printLinkedList())

#Function to save the input as linked list
def makeLinkedList(inputList):
    llist = LinkedList()
    for i in inputList:
        llist.insert(i)

    return llist

#Function to do the addition of the given lists
def addition(llist1, llist2):
    additionLList = LinkedList()
    additionLList.addTwoLinkedList(llist1, llist2)
    return additionLList

#Call the main function
if __name__ == '__main__':
    main()