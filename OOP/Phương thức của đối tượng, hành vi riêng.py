#self là tham số đầu tiên, đại diện cho chính đối tượng gọi phương thức
#khi gọi obj.method(), Python sẽ tự động truyền obj làm dối số self
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    name = input("Please enter your name: ")
    house = input("Please enter your house: ")
    return Student(name,house)
if __name__ == "__main__":
    main()