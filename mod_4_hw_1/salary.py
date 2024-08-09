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

                salary = int(line.split(",")[1])
                total += salary
                employee += 1
                average = int(total / employee)
    
    except FileNotFoundError:
        return f"File not found."

    return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"

print(total_salary(path))