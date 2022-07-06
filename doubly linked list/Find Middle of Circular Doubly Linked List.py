#User function Template for python3

class Solution:
    def findMiddle(self, head):
        #code here
        temp=head
        count=1
        while 1:
            count+=1
            temp=temp.next
            if temp==head:
                break
        count=count//2
        temp=head
        while count-1:
            count-=1
            temp=temp.next
        return temp.data
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


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        # making circular
        tail.next = dll.head
        dll.head.prev = tail

        ob=Solution()
        print(ob.findMiddle(dll.head))




# } Driver Code Ends