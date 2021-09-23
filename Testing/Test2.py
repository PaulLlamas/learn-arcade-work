def hello():
    """ This function prints hello. """
    print("Hello!")


def goodbye():
    print("Goodbye!")


def main():
    hello()
    goodbye()


# Call the main function
    main()

def print_number(my_number):
    print(my_number)


print_number(5)
print_number(6)
print_number(22)

def add_number(a,b):
    print(a + b)


add_number(7, 11)

#Add two numbers and return the results
def sum_two_numbers(a, b):
    result = a + b
    return result

my_result = sum_two_numbers(5, 6)
print(my_result)

def volume_cylinder(radius, height):
    pi = 3.141592653
    volume = pi * radius ** 2 * height
    return volume

my_volume = volume_cylinder(2.5, 5) * 6
print(my_volume)

