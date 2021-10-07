class Room:
    """
    This class represent the room.
    """
    def __init__(self, description, north, east, west, south):
        """ Set up variables in the object """
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south


def main():
    done = False
    room_list = []
    current_room = 0
    room = Room(str("You have just entered a high school through the gate. There is a bench southwest. "
                    "One door that says Business Office east. There is the second part of the hallway south.")
                , None, 1, None, 14)
    room_list.append(room)
    room = Room(str("You just entered the Business Office. There are a couches south."
                    " There is a hallway east. There is a door that says Only Personnel north."
                    "There is a plant southeast"), 2, 5, 0, None)
    room_list.append(room)
    room = Room(str("You just entered the Only Personnel door. There is a desk with papers and a computer."
                    " One door east. Another desk with papers, a computer, and a plant west. There is a "
                    "painting north."), None, 3, None, 1)
    room_list.append(room)
    room = Room(str("You just entered the east door. There is a desk west. There are file cabinets east. There is a "
                    "painting south."), None, 2, None, None)
    room_list.append(room)
    room = Room(str("You walked to the hallway. There is a door west. There are two plants at both sides of"
                    "the door. There is door north that says Accountant."), 4, None, 1, 6)
    room_list.append(room)
    room = Room(str("You just entered the Accountant door. There is a desk east. There is a painting behind"
                    "the desk. There is another painting north. "
                    "There is a couple plants south."), None, None, None, 5)
    room_list.append(room)
    room = Room(str("You enter the door south and now you are in another hallway! There is a door that says"
                    " Counselor east. There is another hallway south."), 5, 7, None, 9)
    room_list.append(room)
    room = Room(str("You enter the door that said Counselor. There is desk south. There is a library with a "
                    "lot of booklets and papers. There is a sofa north. There are flags around the room."), None
                , None, 6, None)
    room_list.append(room)
    room = Room(str("You went to the other hallway. There is a door east. There is the school canteen south. There is"
                    " furniture with trophies in the middle of the room. There is a door west. There is a door"
                    " north."), 12, 8, 14, 10)
    room_list.append(room)
    room = Room(str("You entered the door east. There is a large, empty table in the middle. There is a desk south with"
                    " papers and a telephone. There is a couch north."), None, None, 9, None)
    room_list.append(room)
    room = Room(str("You entered the north door. There is a desk east with paper and a telephone. There is a cabinet "
                    "northeast. There is are two file cabinets north. There is a door saying Principal north west"),
    13, None, None, 9)
    room_list.append(room)
    room = Room(str("You entered the Principal office. There is a desk east with a painting behind it. There are file "
                    "cabinets south. There are plants west of the room. There is a fridge and snacks north"),
    None, None, None, 12)
    room_list.append(room)
    room = Room(str("You entered the school canteen. There are large tables on both north and south part of the room. "
                    "There is a door east saying Only Personnel."), 9, 11, None, None)
    room_list.append(room)
    room = Room(str("You entered the east door. It was the kitchen. There is an island full of equipment in the middle "
                    "of the room. There are freezers south. There is the grill and a sink east. There are pots and "
                    "pans in a furniture in the north."), None, None, 10, None)
    room_list.append(room)
    room = Room(str("You entered an exterior hallway. There is a hallway north. There is a hallway south. There is a "
                    "bench west."), 0, 9, None, 15)
    room_list.append(room)
    room = Room(str("You entered the south side of the hallway. There is absolutely nothing here."),
                14, None, None, None)
    room_list.append(room)

    print("You are in room", current_room)
    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input(str("What do you want to do? "))
        if user_input.lower() == "north" or "n":
            next_room = room_list[current_room].north
        elif user_input.lower() == "east" or "e":
            next_room = room_list[current_room].east
        elif user_input.lower() == "south" or "s":
            next_room = room_list[current_room].south
        elif user_input.lower() == "west" or "w":
            next_room = room_list[current_room].west
        if user_input.lower() == None:
            print("You can't go that way!")
        else:
            print("What do you mean?")


main()