path = "C:/Users/GAME-PC/Documents/My_repo/goit-algo-hw-04/mod_4_hw_2/data-cat.txt"

def get_cats_info(path):
    cat_list = []

    try:
        with open(path, "r", encoding="utf-8") as text:
            for line in text:
                cat_dict = {
                    "id": line.strip().split(",")[0],
                    "name": line.strip().split(",")[1],
                    "age": line.strip().split(",")[2]
                }

                cat_list.append(cat_dict)

        return cat_list

    except FileNotFoundError:
        return f"File not found."


print(get_cats_info(path))