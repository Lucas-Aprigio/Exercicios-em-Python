import random

def gera():
    x=random.randint(1,6)
    return x

def repete (n):
    test1=test2=test3=test4=test5=test6=0
    for val in range(n):
        test = gera()

        if(test==1):
            test1 += 1
        elif (test==2):
            test2 += 1
        elif (test==3):
            test3 += 1
        elif (test==4):
            test4 += 1
        elif (test==5):
            test5 += 1
        else:
            test6 +=1
    print("Numero 1 saiu ", test1, " vezes = ",round((test1/n)*100,2), "%")
    print("Numero 2 saiu ", test2, " vezes = ",round((test2/n)*100,2), "%")
    print("Numero 3 saiu ", test3, " vezes = ",round((test3/n)*100,2), "%")
    print("Numero 4 saiu ", test4, " vezes = ",round((test4/n)*100,2), "%")
    print("Numero 5 saiu ", test5, " vezes = ",round((test5/n)*100,2), "%")
    print("Numero 6 saiu ", test6, " vezes = ",round((test6/n)*100,2), "%")

def menu():
    try:
        n = int(input('Deseja lançar o dado quantas vezes? '))
    except ValueError:
        print ('Atenção: o valor deve ser um ńumero inteiro.')
    except:
        print('Atenção: um erro inesperado aconteceu.')
    try:
        repete(n)
    except:
        print('Tente novamente')

while True:
    menu()

















        
    

    
