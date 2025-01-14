# Write your solution here
def filter_incorrect():
    correct=[]
    with open('lottery_numbers.csv') as file:
        for line in file:
            aux_value=1
            parts=line.strip().split(';')
            aux=parts[0].split()
            try:
                week=int(aux[1])
            except:
                aux_value=0
            lot=parts[1].split(',')
            if len(lot)<7:
                aux_value=0
            for i in range(len(lot)):
                try:
                    if int(lot[i])<1 or int(lot[i])>39:
                        aux_value=0
                except:
                    pass
            for i in range(len(lot)):
                number=lot[i]
                try:
                    aux=int(number)
                except:
                    aux_value=0
                for j in range(len(lot)):
                    if i==j:
                        continue
                    if lot[j]==number:
                        aux_value=0
      
            if aux_value==1:
                correct.append(line)
    with open('correct_numbers.csv','w') as c_file:
        for i in correct:
            c_file.write(i)

