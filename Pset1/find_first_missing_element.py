#######################
###First missing int###
#######################

###Helper function to find s first
def find_s(a, s, init_i = 0):  
    #Base case
    if len(a) == 1:
        return (a[0], init_i) if a[0] == s else None
    
    #Get middle index
    i = int(len(a)/2) 
    
    #Recursive call
    if a[i] == s:
        return (a[i], i + init_i)
    elif a[i] > s:
        return find_s(a[:i], s, init_i)
    else:
        return find_s(a[i:],s, init_i + i)
    
    
###Main function
def first_missing_int(a, s):
    #Base case 
    if len(a) == 1:
        #If there is no missing number in the sequence then the first missing number is the last element plus one.
        #If there is a missing number the answer will also be the last element plus one.
        return a[0] + 1
    
    #Get middle index
    i = int(len(a)/2) 
    
    #Get distance to middle elem
    diff = a[i] - a[0]
    
    #Recursive call
    if diff == i:
        return first_missing_int(a[i:], s)
    else:
        return first_missing_int(a[:i], s)
    
    
###Wrapper function
def find_first_missing_element(a, s): 
    #If list is empty, fme is s. (This check avoids index out of range for empty arrays error)
    if len(a) == 0:
        return s
    
    #First get index of s. (If s wasn't in the array, then s is the fme)
    s_i = find_s(a, s)
    if s_i == None: 
        return s
    else: 
        s_i = s_i[-1]
        
    #Get rid of everything before s 
    a = a[s_i:]
    
    return first_missing_int(a, s)

################################################TESTING####################################################
    
# #Test array
# a = [i for i in range(10,1000000)]
# s = 9880
# a.remove(98801)
# a.remove(98803)

# output = find_first_missing_element(a, s)

# a = [1,2,3,4,5,6]
# s = 7
# output = find_first_missing_element(a, s) 


    