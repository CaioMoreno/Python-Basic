
# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word,n1, n2):
    if len(word)<=n2 or len(word)<=n1 :
        return False
    elif word[n1]==word[n2]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 10))