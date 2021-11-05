def main():
    """ Read in lines from a file """
    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")
    # Create an empty list to store our names
    name_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        name_list.append(line)

    my_file.close()

    print( "There were", len(name_list), "names in the file.")

    key = "Octavia the Siren"
    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
            print(f"Found at position: {middle_pos}")

    if not found:
            print("not found.")

main()