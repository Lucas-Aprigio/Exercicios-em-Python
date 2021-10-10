import random

def gera():
    x = random.randint(0,30)
    return x

def user():
    verif=True
    while verif:
        try:
            z=int(input('Chute um número entre 0 e 30:'))
            verif=False
        except ValueError:
            print('Vamos lá, você não digitou corretamente... Ou ja quer desistir?')
    return z


                   
def brincar(x,z):
    if z==x:
        print('Na mosca!')
    else:
        while z!=x:
            if z>x:
                print('Chute alto! Tente outra vez ou desista!')
            elif z<x:
                print('Chute baixo! Tente outra vez ou desista!')
            try:    
                z=int(input())
            except ValueError:
                print('Você deve digitar um numero inteiro')
                
        print('Demorou mas acertou né?!!!')
        
while True:
    brincar(gera(),user())
