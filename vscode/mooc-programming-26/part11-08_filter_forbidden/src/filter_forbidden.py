# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    #return "".join([word if word not in list(forbidden) else "" for word in list(string)])
    return "".join(word for word in string if word not in forbidden)

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)