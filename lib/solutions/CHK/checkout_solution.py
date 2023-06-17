# noinspection PyUnusedLocal
# skus = unicode string

item_price_map = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

item_bogof_map = {
    "E": {2: "B"},
    "F": {2: "F"},
    "N": {3: "M"},
    "R": {3: "Q"},
    "U": {3: "U"},
}

item_multi_price_map = {
    "A": {3: 130, 5: 200},
    "B": {2: 45},
    "H": {5: 45, 10: 80},
    "K": {2: 150},
    "P": {5: 200},
    "Q": {3: 80},
    "V": {2: 90, 3: 130},
}


def calculate_multi_price(total: int, item: str, count: int):
    if len(item_multi_price_map[item]) == 2:
        max_key = max(item_multi_price_map[item].keys())
        div, remainder = divmod(count, max_key)
        total += div * item_multi_price_map[item][max_key]
        min_key = min(item_multi_price_map[item].keys())
        div, remainder = divmod(remainder, min_key)
        total += div * item_multi_price_map[item][min_key]
        total += remainder * item_price_map[item]
    elif len(item_multi_price_map[item]) == 1:
        div, remainder = divmod(item, 2)
        total += div * 45
        total += remainder * 30
    else:
        raise ValueError("Too many multiprice offers. Implement.")


def calculate_price(item_count: dict) -> int:
    total = 0
    for item, count in item_count.items():
        if item in item_multi_price_map.keys():
            calculate_multi_price(total, item, count)

    total = calculate_A(total, item_count)
    total = calculate_E(total, item_count)
    total = calculate_B(total, item_count)
    total = calculate_C(total, item_count)
    total = calculate_D(total, item_count)
    total = calculate_F(total, item_count)
    return total


def checkout(skus):
    item_count = {}
    for item in skus:
        if item not in item_price_map.keys():
            return -1
        if item in item_count.keys():
            item_count[item] += 1
        else:
            item_count[item] = 1
    return calculate_price(item_count)


#####
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
        total += item_count["F"] * 10
        div, _ = divmod(item_count["F"], 3)
        total -= div * 10
    return total


def calculate_price(item_count: dict) -> int:
    total = 0
    total = calculate_A(total, item_count)
    total = calculate_E(total, item_count)
    total = calculate_B(total, item_count)
    total = calculate_C(total, item_count)
    total = calculate_D(total, item_count)
    total = calculate_F(total, item_count)
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


