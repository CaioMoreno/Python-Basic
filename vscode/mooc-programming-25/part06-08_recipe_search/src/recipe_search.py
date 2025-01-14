# Write your solution here
def search_by_name(filename: str, word: str):
    list_recipe=[]
    new_list=[]
    with open (filename) as file:
        for line in file:
            list_recipe.append(line.strip())
        for i in range(len(list_recipe)):
            if word.lower() in list_recipe[i].lower():
                novo=list_recipe[i]
                if novo[0].isupper():
                    new_list.append(list_recipe[i])
    return new_list          

def search_by_time(filename: str, prep_time: int):
    list_recipe=[]
    new_list=[]
    with open (filename) as file:
        for line in file:
            part=line.strip()
            if part=="":
                continue
            elif part[0].isupper():
                list_recipe.append(part) 
            elif part.isdigit():
                list_recipe.append(part)

        for i in range(len(list_recipe)-1):
            if list_recipe[i+1].isdigit():
                if int(list_recipe[i+1])<=prep_time:
                    new_list.append(f'{list_recipe[i]}, preparation time {list_recipe[i+1]} min')
        return new_list

def search_by_ingredient(filename: str, ingredient: str):
    list_recipe=[]
    new_list=[]
    with open (filename) as file:
        for line in file:
            part=line.strip()
            list_recipe.append(part)
            if part=="":
                if ingredient in list_recipe:
                    new_list.append(f'{list_recipe[0]}, preparation time {list_recipe[1]} min')
                list_recipe.clear()
        if ingredient in list_recipe:
                new_list.append(f'{list_recipe[0]}, preparation time {list_recipe[1]} min')
                list_recipe.clear()
        return new_list