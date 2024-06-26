# Insertion sort algorithm implementation

def insertion_sort(elements):
    # Iterate over the list starting from the second element
    for i in range(1, len(elements)):
        # The element to be positioned in the sorted portion of the list
        anchor = elements[i]
        # Index of the last element in the sorted portion of the list
        j = i - 1
        # Move elements of the sorted portion of the list that are greater than the anchor to one position ahead of their current position
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        # Place the anchor in its correct position
        elements[j + 1] = anchor

# Main block to test the insertion sort function
if __name__ == '__main__':
    # Example list of integers
    #elements = [11, 9, 29, 7, 2, 15, 28]
    elements = [11, 29, 7]
    insertion_sort(elements)
    print(elements)  # Output: [2, 7, 9, 11, 15, 28, 29]

    # List of test cases
    '''tests = [
        [11, 9, 29, 7, 2, 15, 28],  # Unsorted list
        [3, 7, 9, 11],              # Already sorted list
        [25, 22, 21, 10],           # Reverse sorted list
        [29, 15, 28],               # Short list
        [],                         # Empty list
        [6]                         # Single element list
    ]

    # Sort each test case and print the sorted list
    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
'''