def square_of_hashes(size):
    # You should call function line here with proper parameters
    aux=size
    while aux >0:
        line(5, "#", size)
        aux-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)