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
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

item_bogof_map = {
    "E": {2: "B"},
    "F": {3: "F"},
    "N": {3: "M"},
    "R": {3: "Q"},
    "U": {4: "U"},
}

item_multi_price_map = {
    "A": {3: 130, 5: 200},
    "B": {2: 45},
    "H": {5: 45, 10: 80},
    "K": {2: 120},
    "P": {5: 200},
    "Q": {3: 80},
    "V": {2: 90, 3: 130},
}


def calculate_multi_price(total: int, item: str, count: int):
    """Using the multiprice offer, add to the total value."""
    keys_sorted = sorted(item_multi_price_map[item].keys(), reverse=True)
    for key in keys_sorted:
        div, count = divmod(count, key)
        total += div * item_multi_price_map[item][key]
    total += count * item_price_map[item]
    print(item, total)
    return total


def calculate_bogof_price(item_count: dict, total: int, item: str, count: int):
    """Using the BOGOF offer, add to the total value."""
    num, free_item = (
        list(item_bogof_map[item].keys())[0],
        list(item_bogof_map[item].values())[0],
    )
    div, remainder = divmod(count, num)
    if free_item in item_count.keys():
        item_count[free_item] -= div
        if item_count[free_item] < 0:
            item_count[free_item] = 0
    total += item_count[item] * item_price_map[item]
    return total


def calculate_price(item_count: dict) -> int:
    """Calculate total price by applying BOGOF offers first, multiprice offers,
    and then any remaining items."""
    total = 0
    for item in item_bogof_map.keys():
        if item in item_count.keys():
            total = calculate_bogof_price(item_count, total, item, item_count[item])
            item_count.pop(item)
    for item in item_multi_price_map.keys():
        if item in item_count.keys():
            total = calculate_multi_price(total, item, item_count[item])
            item_count.pop(item)
    for item in item_count.keys():
        total += item_count[item] * item_price_map[item]
    return total


def checkout(skus):
    """Calculate price from string of items."""
    item_count = {}
    for item in skus:
        if item not in item_price_map.keys():
            return -1
        if item in item_count.keys():
            item_count[item] += 1
        else:
            item_count[item] = 1
    return calculate_price(item_count)
