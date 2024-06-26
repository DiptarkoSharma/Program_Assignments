
def swap(a,b,arr):
    if a!=b:
        arr[a],arr[b]=arr[b],arr[a]


def partition_elements(elements,start,end):
    pass
    #Set the pivot
    pivot_index = start
    pivot = elements[pivot_index]

    #Set the start point to pivot index +1
    start = pivot_index+1
    #Set the end point to end of array
    end = len(elements)-1

    while start <= end : #As long as end point doesnt crossover start point
        #Hoares partition, first start with the start point
        #Rule: Move the start till you encounter a point > Pivot
        #Also ennsure that during the increment process start doesnt overshoot the
        #last index.
        while   start < len(elements) and pivot >= elements[start] :
            start+=1
            #Stop when element found which is > pivot
        #Now lets work with the end point
        #Rule : move backwards the end point till you get an element < pivot
        while elements[end] > pivot:            
            end -=1
        
        #When the end point stops at an element which is less than Pivot,
        #swap start and stop
        if start < end:
            swap(start,end,elements) 
    #If end crosses the start poistion swap the elemnt at end with pivot
    swap(pivot_index,end,elements)   
    return end
    
            

def quick_sort(elements,start,end):
    #Returns the index at which the last iteration had stopped.

    if start < end:
        pi = partition_elements(elements,start,end)
        quick_sort(elements,start,pi-1)#Left sort
        quick_sort(elements,pi+1,end)#Right sort


if __name__=='__main__':
    elements = [11,9,29,7,2,15,28]
    #elements = [3, 7, 9, 11]
    print(elements)
    start = 0
    end = len(elements)-1
    quick_sort(elements,start,end)
    print(elements)
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
