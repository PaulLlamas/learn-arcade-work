def main():
    my_file = open("super_villains.txt")
    list = []
    for line in my_file:
        line = line.strip()
        list.append(line)
    my_file.close()
    print(list)
    print(f"The are {len(list)} names in the list.")

    # Linear search
    key = "The Forsaken Succubus"

    current_list_position = 0
    while current_list_position < len(list) and list[current_list_position] != key:
        current_list_position += 1

    if current_list_position < len(list):
        print(f"Found at {current_list_position}")
    else:
        print("Not found.")

    # Inverse
    if current_list_position >= len(list):
        print("Not found.")


main()