# Write your solution here:
def sort_by_seasons(items: list):
    def order_by_seasons(item: dict):
        key = list(item.keys())[2]
        return item[key]
    return sorted(items, key=order_by_seasons)

