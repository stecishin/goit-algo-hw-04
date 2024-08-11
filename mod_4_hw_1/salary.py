path = "C:/Users/GAME-PC/Documents/My_repo/goit-algo-hw-04/mod_4_hw_1/data-salary.txt"

def total_salary(path):
    total = 0
    employee = 0

    try:
        with open(path, "r", encoding="utf-8") as text:
            while True:
                line = text.readline()
                if not line:
                    break

                salary = float(line.split(",")[1])
                total += salary
                employee += 1
                
            if employee > 0:
                average = total / employee
            else:
                average = 0
    
    except FileNotFoundError:
        return f"File not found."

    return total, average

print(total_salary(path))