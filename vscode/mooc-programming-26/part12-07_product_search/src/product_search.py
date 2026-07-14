# Write your solution here
def search(products: list, criterion: callable):
    
    aux = [product for product in products if criterion(product)]
    return aux

