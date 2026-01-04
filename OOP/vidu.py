grade = int(input("Grade:"))
if grade < 0 or grade > 100:
    raise ValueError("Grade must be between 0 and 100")