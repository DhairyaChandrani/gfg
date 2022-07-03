#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

def sortedInsert(head, x):
    #code here
    temp=Node(x)
    c1=head
    if head==None:
        return temp
       
    if head.data>temp.data:
        temp.next=head
        head.prev=temp
        return temp
       
    if head.next==None:
        head.next=temp
        temp.prev=head
        return head
       
    while c1.next.data<temp.data:
        c1=c1.next
        if c1.next==None:
            break
   
    if c1.next==None:
        c1.next=temp
        temp.prev=c1
        return head
    else:
        temp.next=c1.next
        c1.next.prev=temp
        temp.prev=c1
        c1.next=temp
        return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


def displayList(head):
    pvs=None
    while head:
        print(head.data, end=' ')
        if head.prev !=pvs:
            print('prev pointer not connected')
        pvs = head
        head = head.next
        


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        dll.head=sortedInsert(dll.head, x)
        displayList(dll.head)
        print()




# } Driver Code Ends