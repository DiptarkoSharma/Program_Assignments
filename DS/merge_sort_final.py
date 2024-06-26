def merge_sort(arr):#recursively Divide and then conquer
    if len(arr) <= 1:
        return
    #Finding midpoint for partition
    mid = len(arr)//2
    #Split the array recursively
    left = arr[:mid]
    right = arr[mid:]
    #Recursively sort the array
    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)
#Function for merging two sorted arrays
def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:#Continue loop long as both the indexes stay 
        #within their respective bounds
        #If element pointed by pointer i in left bound is less than than in right
        #  bound
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        #If element pointed by pointer j in right bound is greater than than in right
        #  bound
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    #Handle any left over cases after the common merge. 
    #Maybe array a has more elements than b
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    #Handle any left over cases after the common merge. 
    #Maybe array b has more elements than c
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)
