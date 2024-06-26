# Bubble sort algorithm implementation
# This function can be used to sort a list of elements, including strings

def bubble_sort(elements):
    # Get the size of the list
    size = len(elements)

    # Loop through the list size-1 times
    for i in range(size-1):
        # Track if any elements were swapped during this pass
        swapped = False

        # Inner loop for comparing adjacent elements
        for j in range(size-1-i):
            # If the current element is greater than the next element, swap them
            if elements[j] > elements[j+1]:
                # Swap the elements
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                # Set swapped to True indicating a swap occurred
                swapped = True

        # If no elements were swapped, the list is sorted, break out of the loop
        if not swapped:
            break

# Main block to test the bubble sort function
if __name__ == '__main__':
    # Example list of integers
    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)  # Output: [1, 2, 5, 9, 34, 34, 67, 88]

    # Example list with repeated integers
    elements = [1,2,3,4,2]
    bubble_sort(elements)
    print(elements)  # Output: [1, 2, 2, 3, 4]

    # Example list of strings
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    print(elements)  # Output: ['aamir', 'chang', 'dhaval', 'mona', 'tina']
