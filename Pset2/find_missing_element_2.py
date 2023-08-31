import math
##################################################
##  Problem 3.c. Find the Missing Number 2
##################################################

# Given n integers in the range [0,N] where n <= N, find an integer
# in the range [0,N] that is missing. If there are multiple missing numbers,
# return any of them. There is at least one number in the range that is missing.
def merge_sort(A, a = 0, b = None):
    if b is None: b = len(A)
    if 1 < b - a: # O(1)
        c = (a + b + 1) // 2 
        merge_sort(A, a, c) 
        merge_sort(A, c, b) 
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b) 

def merge(L, R, A, i, j, a, b):
    if a < b: 
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]): 
            A[b - 1] = L[i - 1] 
            i = i - 1 
        else: 
            A[b - 1] = R[j - 1] 
            j = j - 1 
        merge(L, R, A, i, j, a, b - 1) 



def find_missing_int(arr, N):
    '''
    Inputs:
        arr     (list(int)) | List of unsorted, unique positive integer order id's
        N       (int)       | A positive integer larger than len(arr)
    Output:
        -       (int)       | An integer in the range [0,N] not present in arr
    '''

    ##################
    # YOUR CODE HERE #
    ################## 
    n = len(arr)
    if n > 0 and N <= n*math.log(n, 2):
        daa = [None]*(N+1)
        for elem in arr:
            daa[elem] = elem
            
        for i in range(N+1):
            if daa[i] == None:
                return i 
        
        return N
    else:
        if n == 0: 
            return N
        merge_sort(arr)
        first = arr[0]
        if first != 0:
            return 0
        for elem in arr[1:]:
            if elem - first != 1:
                return first + 1
            first = elem
            
        return N 
        
        
        

# print(find_missing_int([0,1,3,4],4))
# print(find_missing_int([6,2,4,5,0,1,3],7))
# print(find_missing_int([6,8,3,2],8))
        
