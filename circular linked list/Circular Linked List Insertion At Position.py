#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def insertAtPosition(head,pos,data):
    #code here
    temp = Node(data)
    if pos == 0:
        temp.next = head.next
        head.next = temp
        temp.data,head.data = head.data,temp.data
        return head
    else:
        curr = head
        while pos-1:
            pos-=1
            curr = curr.next
            if curr == head:
                return head
        temp.next = curr.next
        curr.next = temp
        return head
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def displayList(head):
    t=head
    while t.next!=head:
        print(t.data,end=' ')
        t=t.next
    print(t.data,end=' ')


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        pos,data=[int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)
        #making circular
        tail.next=ll.head

        insertAtPosition(ll.head,pos,data)
        displayList(ll.head)
        print()
# } Driver Code Ends