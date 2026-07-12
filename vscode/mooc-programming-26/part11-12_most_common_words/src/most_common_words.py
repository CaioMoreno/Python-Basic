# WRITE YOUR SOLUTION HERE:
def most_common_words(filename:str, lower_limit: int):
    ponctuation = "!?:,."
    with open(filename, "r", encoding="utf-8") as file:
        file_text = file.read()
        main_list = "".join(words for words in file_text if words not in ponctuation).split()
        
    words_count = {word : main_list.count(word) for word in set(main_list)}
    result = {word : count for word, count in words_count.items() if count >= lower_limit}
    return result




