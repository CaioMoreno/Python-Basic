# Write your solution here
def create_tuple(x: int, y: int, z: int):
    soma=x+y+z
    if x>y and y>z:
        tuple=(z, x, soma)
    elif x>z and z>y:
        tuple=(y, x, soma)
    elif y>z and z>x:
        tuple=(x, y, soma)
    elif y>x and x>z:
        tuple=(z, y, soma )
    elif z>x and x>y:
        tuple=(y, z, soma)
    elif z>y and y>x:
        tuple=(x, z, soma)
    return tuple
    
        

