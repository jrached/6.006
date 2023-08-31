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
    daa = [None]*(N+1)
    for elem in arr:
        daa[elem] = elem
        
    for i in range(N+1):
        if daa[i] == None:
            return i 
    
    return N


