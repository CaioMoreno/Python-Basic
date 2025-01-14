# Write your solution here
def longest(strings: list):
    tam=len(strings)
    string=""
    for i in range(tam):
        if len(strings[i]) > len(string):
            string=strings[i]
    return string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
