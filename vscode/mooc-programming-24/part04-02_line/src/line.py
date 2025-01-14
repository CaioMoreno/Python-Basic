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