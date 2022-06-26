#User function Template for python3

def deleteTail(head):
    #code here
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
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

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res=deleteTail(ll.head)
        printList(res)
        print()
# } Driver Code Ends