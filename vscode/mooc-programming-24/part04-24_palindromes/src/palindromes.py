# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string):
    return string == string[::-1]  # Check if the string is the same forwards and backwards

# Main program
while True:
    string = input("Please type in a palindrome: ")
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break  # Exit the loop if a palindrome is found
    else:
        print("that wasn't a palindrome")



