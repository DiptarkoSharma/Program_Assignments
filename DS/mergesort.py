def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = (len(arr))//2

    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    
    sorted_arr =  merge_two_sorted_arrays(left,right,arr)
    return sorted_arr

def merge_two_sorted_arrays(a,b,arr):
    sorted_array = []

    i = j= k=0 #set both the pointers at 0
    len_a = len(a)
    len_b = len(b)
    #Continue loop long as both the indexes stay within their respective bounds
    while i < len_a-1 and j < len_b-1: 
        #If element pointed by pointer i in left bound is less than than in right bound
        if a[i] >= b[j]:
            #arr[k] = b[j]
            sorted_array.append(b[j]) 
            j+=1
        #If element pointed by pointer j in right bound is greater than than in right bound
        else:
            arr[k] = a[i]
            sorted_array.append(a[i])
            i+=1
    while i < len_a-1:
    #Handle any left over cases after the common merge. 
    #Maybe array a has more elements than b
        arr[k] = a[i]
        sorted_array.append(a[i])
        i+=1
        #k+=1
    while j < len_b-1:
    #Handle any left over cases after the common merge. 
    #Maybe array a has more elements than b
        arr[k] = b[j]
        sorted_array.append(b[j])
        j+=1
        #k+=1
    return sorted_array
        

if __name__ =='__main__':
    '''a = [17,21,34,60]
    b = [8,12,30]

    merge_sort(array)
    arr = []

    print(merge_two_sorted_arrays(a,b,arr))'''
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    '''for arr in test_cases:
        merge_sort(arr)
        print(arr)'''
    arr = [9,8,7,2]