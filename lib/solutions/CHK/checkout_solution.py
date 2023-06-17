# noinspection PyUnusedLocal
# skus = unicode string
def calculate_price(item_count: dict) -> int:
    total = 0
    div, remainder = divmod(item_count["A"], 3)
    total += div * 130
    total += remainder * 50
    div, remainder = divmod(item_count["B"], 2)
    total += div * 45
    total += remainder * 30
    total += item_count["C"] * 20
    total += item_count["D"] * 15
    return total


def checkout(skus):
    item_count = {}
    for item in skus:
        if item in item_count.keys():
            item_count[item] += 1
        else:
            item_count[item] = 1
    return calculate_price(item_count)

