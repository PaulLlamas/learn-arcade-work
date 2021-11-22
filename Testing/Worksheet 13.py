import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """
    sel_out_count = 0
    sel_in_count = 0
    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
        sel_out_count += 1

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):

            sel_in_count += 1
            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    print(f"The ouside loop looped {sel_out_count} times")
    print(f"The inside loop looped {sel_in_count} times")


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    ins_out_count = 0
    ins_in_count = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)): # 100

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        ins_out_count += 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # Worst 50, avg - 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
            ins_in_count += 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
    print(f"The ouside loop looped {ins_out_count} times")
    print(f"The inside loop looped {ins_in_count} times")


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()