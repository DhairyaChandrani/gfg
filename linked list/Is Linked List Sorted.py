#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def isSorted(head):
    #code here
    cur = head
   
    is_inc = True 
    is_dec = True 
   
    while cur is not None and cur.next is not None: 
        is_inc = is_inc and cur.data <= cur.next.data
        is_dec = is_dec and cur.data >= cur.next.data
        cur = cur.next

    res = int(is_inc or is_dec)
    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
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


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res=isSorted(ll.head)
        print(res)
# } Driver Code Ends