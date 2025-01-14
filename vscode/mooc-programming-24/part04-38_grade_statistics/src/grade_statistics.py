# Write your solution here

def count_points():
    question = "a"
    total=[]
    while question != "":
        question = input("Exam points and exercises completed: ")
        total.append(question)
    return total

def print_average(med):
    print(f"Points average: {med:.1f}")

def pass_percentage(percent):
    tam=len(percent)
    sum=0
    for i in range(tam):
        if percent[i]!=0:
            sum+=1
    med=(sum/(tam))*100
    return med
            

def count_grade(calc):
    tam=len(calc)
    exam=0
    exercise=0
    final=[]
    average=0

    for i in range (tam-1):
        note=calc[i].split()
        if len(note)<2:
            break
   
        exam=int(note[0])
        exercise=int(note[1])
        exercise=exercise/10
        exercise=exercise//1

        all=exam+exercise

        if all<=14 or exam < 10:
            final.append(0)
        elif all<=17:
            final.append(1)
        elif all<=20:
            final.append(2)
        elif all<=23:
            final.append(3)
        elif all<=27:
            final.append(4)
        elif all<=30:
            final.append(5)

        average+=all
    average=average/(tam-1)
    print_average(average)
    
    return final
        
def grade_distribution(dist):
    zero=""
    one=""
    two=""
    three=""
    four=""
    five=""
    tam=len(dist)
    i=-1

    for i in range (tam):
        if dist[i]==0:
            zero+="*"
        elif dist[i]==1:
            one+="*"
        elif dist[i]==2:
            two+="*"
        elif dist[i]==3:
            three+="*"
        elif dist[i]==4:
            four+="*"
        elif dist[i]==5:
            five+="*"
    print(f"5: {five}")
    print(f"4: {four}")
    print(f"3: {three}")
    print(f"2: {two}")
    print(f"1: {one}")
    print(f"0: {zero}")

def main():

    points=count_points()
    print("Statistics:")
    grade=count_grade(points)
    media=pass_percentage(grade)
    print(f"Pass percentage: {media:.1f}")
    print("Grade distribution:")
    grade_distribution(grade)

main()