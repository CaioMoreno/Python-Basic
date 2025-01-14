
# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        s=0
        for line in new_file:
            n=line.split(',')
            for i in range(len(n)):
                s+=int(n[i])
        return s

def matrix_max():
    with open("matrix.txt") as new_file:
        m=0
        for line in new_file:
            n=line.split(',')
            for i in range(len(n)):
                if m<int(n[i]):
                    m=int(n[i])
        return m

def row_sums():
    with open("matrix.txt") as new_file:
        l=[]
        for line in new_file:
            s=0
            n=line.split(',')
            for i in range(len(n)):
                s+=int(n[i])
            l.append(s)
        return l


