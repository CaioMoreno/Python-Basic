# Copy here code of line function from previous exercise

def line(n, l):
    if(l==""):
        print(n*"*")
    else:
        print(n*l[0])

def triangle(size):
    # You should call function line here with proper parameters
    aux=size
    i=1
    while aux >0:
        line(i, "#")
        i+=1
        aux-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
