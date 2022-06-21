#User function Template for python3

class Solution:
    def merge(self,a, low, mid, high): 
        # code here
        left = a[low:mid + 1]
        right = a[mid + 1:high + 1]

        i = j = 0
        k = low

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                a[k] = left[i]

                k += 1
                i += 1
            else:
                a[k] = right[j]
                k += 1
                j += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        
        
    def mergeSort(self,arr, l, r):
        #code here
        if r > l:
            m = (r + l) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends