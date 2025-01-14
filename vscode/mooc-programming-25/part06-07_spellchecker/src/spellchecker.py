# write your solution here
text=input("Write text: ")
palavras_text=text.split()
list_text=[]
with open ('wordlist.txt') as file:
    for line in file:
        list_text.append(line.strip())

    for palavra in palavras_text:
        if palavra.lower() not in list_text:
            index=palavras_text.index(palavra)
            palavras_text[index]=f'*{palavra}*'
    frase=" ".join(palavras_text)
    print(frase)