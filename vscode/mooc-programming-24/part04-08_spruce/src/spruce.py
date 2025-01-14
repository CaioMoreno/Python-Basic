# Write your solution here
def spruce(n):
    print("a spruce!")
    i=0
    j=n-1
    l=1
    while i<n:
        print(f"{j*" "}{l*"*"}")
        j-=1
        l+=2
        i+=1
    print(f"{(n-1)*" "}{"*"}")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)