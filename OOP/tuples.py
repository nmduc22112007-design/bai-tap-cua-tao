#vd1
coordinates = (10,20)
x, y = coordinates
print(f"x: {x}, y: {y}")
#vd2:
def main():
    name,house = get_student()
    print(f"name: {name} from house {house}")
def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return name,house
if __name__ == "__main__":
    main()
