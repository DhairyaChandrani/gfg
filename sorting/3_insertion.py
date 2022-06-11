#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        while index>=0 and n<alist[index]:
            alist[index+1] = alist[index]
            index = index-1
        alist[index+1] = n
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(1,n):
            j = i-1
            x = alist[i]
            self.insert(alist,j,x)

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends