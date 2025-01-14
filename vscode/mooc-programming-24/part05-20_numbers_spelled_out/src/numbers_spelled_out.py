# Write your solution here
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    numbers_dict = {}

    for i in range(100):
        if i < 10:
            numbers_dict[i] = ones[i]  # 0-9
        elif 10 <= i < 20:
            numbers_dict[i] = teens[i - 10]  # 10-19
        else:
            ten_part = tens[i // 10]  # Tens place (20, 30, ..., 90)
            one_part = ones[i % 10] if i % 10 != 0 else ""  # Ones place
            numbers_dict[i] = f"{ten_part}-{one_part}".strip("-")  # Handle cases like 20, 30
    return numbers_dict

