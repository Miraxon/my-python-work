grades={'Karim':[10,20,30],'Mohamed':[30,25,35]}
for key,value in grades.items():
    print(f'{key} average score is {sum(value)/3}')