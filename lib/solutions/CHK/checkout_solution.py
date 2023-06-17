# noinspection PyUnusedLocal
# skus = unicode string


def calculate_A(total: int, item_count: dict):
    if "A" in item_count.keys():
        div, remainder = divmod(item_count["A"], 5)
        total += div * 200
        div, remainder = divmod(remainder, 3)
        total += div * 130
        total += remainder * 50
    return total


def calculate_B(total: int, item_count: dict):
    if "B" in item_count.keys():
        div, remainder = divmod(item_count["B"], 2)
        total += div * 45
        total += remainder * 30
    return total


def calculate_C(total: int, item_count: dict):
    if "C" in item_count.keys():
        total += item_count["C"] * 20
    return total


def calculate_D(total: int, item_count: dict):
    if "D" in item_count.keys():
        total += item_count["D"] * 15
    return total


def calculate_E(total: int, item_count: dict):
    if "E" in item_count.keys():
        div, remainder = divmod(item_count["E"], 2)
        if "B" in item_count.keys():
            item_count["B"] -= div
            if item_count["B"] < 0:
                item_count["B"] = 0
        total += item_count["E"] * 40
    return total


def calculate_F(total: int, item_count: dict):
    if "F" in item_count.keys():
        div, remainder = divmod(item_count["F"], 2)
        item_count["F"] -= div
        if item_count["F"] < 0:
            item_count["F"] = 0
        total += item_count["F"] * 10


def calculate_price(item_count: dict) -> int:
    total = 0
    total = calculate_A(total, item_count)
    total = calculate_E(total, item_count)
    total = calculate_B(total, item_count)
    total = calculate_C(total, item_count)
    total = calculate_D(total, item_count)
    return total


def checkout(skus):
    item_count = {}
    for item in skus:
        if item not in ["A", "B", "C", "D", "E", "F"]:
            return -1
        if item in item_count.keys():
            item_count[item] += 1
        else:
            item_count[item] = 1
    return calculate_price(item_count)




