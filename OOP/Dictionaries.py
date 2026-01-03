def main():
    student = get_student()
    print(f"{student["name"]} from {student['house']}")
def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return {"name": name, "house": house}
if __name__ == "__main__":
    main()