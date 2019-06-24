from pprint import pprint
import yaml

CARDINALS = ["north", "east", "south", "west"]


def _load_data(file_name_and_path="./dork/maze.yml"):
    with open(file_name_and_path) as file:
        data = yaml.safe_load(file.read())

    return data
    
    
def _check_path(rooms, name, direction):
    room = rooms[name]
    if direction not in room:
        print(f"{name} does not have {direction} as a key.")
    elif room[direction] is None:
        print(f"There is nothing {direction} of {name}.")
    elif room[direction] not in rooms:
        print(f"Going {direction} of {name} leads to an error!")
    else:
        other = room[direction]
        print(f"{other} is {direction} of {name}")


def main():
    data = _load_data()
    print("loaded this data: ")
    pprint(data)

    print("checking that data contains a dictionary of rooms...")
    if "Rooms" not in data:
        print("No Rooms found.")
        return

    if not isinstance(data["Rooms"], dict):
        print("Rooms in data was not proper data.")
        return

    rooms = data["Rooms"]
    for name in rooms:
        for direction in CARDINALS:
            _check_path(rooms, name, direction)


if __name__ == "__main__":
    main()