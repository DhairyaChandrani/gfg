#User function Template for python3

class Solution:
    def compareCLL(self,head1,head2):
        #code here
        curr1 = head1
        curr2 = head2
        
        while curr1.next != head1 or curr2.next != head2:
            if curr1.data == curr2.data:
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                return 0
        if curr1.data == curr2.data:
            return 1
        else: 
            return 0
        return 1
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

def getLength(head):
    temp=head
    count=1
    while(temp.next!=head):
        temp=temp.next
        count+=1
    return count
    

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        n2=int(input())
        arr2=[int(x) for x in input().split()]

        dll1=doublyLL()
        tail=None
        for nodeData in arr1:
            tail=dll1.insert(tail,nodeData)

        # making circular
        tail.next = dll1.head
        dll1.head.prev = tail

        dll2 = doublyLL()
        tail = None
        for nodeData in arr2:
            tail = dll2.insert(tail, nodeData)

        # making circular
        tail.next = dll2.head
        dll2.head.prev = tail
        ob=Solution()
        if(ob.compareCLL(dll1.head,dll2.head)):
            print(1)
        else:
            print(0)




# } Driver Code Ends