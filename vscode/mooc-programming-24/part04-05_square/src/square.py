# Copy here code of line function from previous exercise

def line(n, l, s):
    n=s
    if(l==""):
        print(n*"*")
    else:
        print(n*l[0])

def square(size, character):
    # You should call function line here with proper parameters
    aux=size
    while aux >0:
        line(5, character, size)
        aux-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")