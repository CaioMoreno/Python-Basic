# Write your solution here
# You can test your function by calling it within the following block
def line(n, l):
    i=0
    if(l==""):
        print(n*"*")
    else:
        print(n*l[0])

if __name__ == "__main__":
    line(5, "")


# Copy here code of line function from previous exercise
def line(n, l, s):
    n=s
    if(l==""):
        print(n*"*")
    else:
        print(n*l[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    aux=size
    while aux >0:
        line(5, "#", size)
        aux-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":