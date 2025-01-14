# Write your solution here
def invert(dictionary: dict):
    aux={}
    for key, value in dictionary.items():
        aux[value]=key
    print(aux)
    dictionary.clear()
    for key, value in aux.items():
        dictionary[key]=value

