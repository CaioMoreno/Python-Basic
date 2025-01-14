# Write your solution here
def find_words(search_term: str):
    contain=[]
    with open('words.txt') as file:
        if '.' in search_term:
            tam=len(search_term)
            local=[]
            v=0
            for i in range(tam):
                        if search_term[i]!='.':
                            local.append(i)
            for line in file:
                word = line.strip()
                if len(word) == tam:
                    for i in range(len(local)):
                        if word[local[i]]==search_term[local[i]]:
                            print(search_term[local[i]])
                            v=1       
                        else:
                            v=0
                            break
                    if v==1:
                        contain.append(word)

        elif '*' in search_term:
            new_word=search_term.strip('*')
            for line in file:
                word=line.strip()
                if search_term.startswith('*'):
                    if word.endswith(new_word):
                        contain.append(word)
                elif search_term.endswith('*'):
                    if word.startswith(new_word):
                        contain.append(word)
        
        else:
            for line in file:
                word = line.strip()
                if word == search_term:
                    contain.append(word)

        return contain



