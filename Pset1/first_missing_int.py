#######################
###First missing int###
#######################

class Counter():
    def __init__(self, init_val):
        self.val = init_val

    def count(self):
        self.val += 1
    
    def get_count(self):
        return self.val
    
#Counter to get a sense for runtime
steps = Counter(0)        

###Helper function to find s first
def find_s(a, s, steps = None, init_i = 0):  
    #Count to get a sense for runtime
    if steps is not None:
        steps.count()
    
    #Base case
    if len(a) == 1:
        return (a[0], init_i) if a[0] == s else None
    
    #Get middle index
    i = int(len(a)/2) 
    
    #Recursive call
    if a[i] == s:
        return (a[i], i + init_i)
    elif a[i] > s:
        return find_s(a[:i], s, steps, init_i)
    else:
        return find_s(a[i:],s, steps, init_i + i)
    
    
###Main function
def first_missing_int(a, s, steps = None, s_i = None, missing_num = False):
    #First get index of s. (If s wasn't in the array, then s is the first missing element)
    if s_i is None:
        s_i = find_s(a, s, steps)
        if s_i == None:
            print("Missing num is s")
            return s
        else:
            s_i = s_i[-1]
        a = a[s_i+1:]
        
    #Count to get a sense for runtime
    if steps is not None:
        steps.count()
    
    #Base case 
    if len(a) == 1:
        print("Missing num? " + str(missing_num))
        return a[0] + 1 if missing_num else None
    if len(a) == 0:
        #In case the array of len() = 0 bug happens again
        print("This should never happen")
        return None
    
    #Get middle index
    i = int(len(a)/2) 
    
    #Get distance to middle elem
    diff = a[i] - a[0]
    
    #Recursive call
    if diff == i:
        return first_missing_int(a[i:], s, steps, s_i, missing_num)
    else:
        missing_num = True
        return first_missing_int(a[:i], s, steps, s_i, missing_num)
    
    
###Wrapper function for testing
def find_first_missing_element(a, s):
    return first_missing_int(a, s)

######################################################TESTING####################################################
    
# #Test array
# a = [i for i in range(10,100000)]
# s = 9880
# a.remove(98800)
# a.remove(98803)

# #With runtime analysis (for testing mostly)
# output = first_missing_int(a, s, steps)  
# print("\nTook " + str(steps.get_count()) + " steps")

# #Without runtime analysis (what you should put through the staff tests)
# output = find_first_missing_element(a, s)
    