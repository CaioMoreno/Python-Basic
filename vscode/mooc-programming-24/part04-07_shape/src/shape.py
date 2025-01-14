# Copy here code of line function from previous exercise and use it in your solution
def line(n, l):
    i=0
    if(l==""):
        print(n*"*")
    else:
        print(n*l[0])

# You can test your function by calling it within the following block
def shape(st,t,sr,r):
    auxt=st
    auxr=sr
    i=1
    while auxt >0:
        line(i, t)
        i+=1
        auxt-=1
    while auxr>0:
        line(st,r)
        auxr-=1

    

if __name__ == "__main__":
    shape(5, "x", 2, "o")