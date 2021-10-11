# Exercício 1

class Livro:

    def __init__(self, titulo_livro, aut_livro, num_pag):
        self.titulo=titulo_livro
        self.autor=aut_livro
        self.num_paginas= num_pag

pequeno_principe=Livro('O pequeno principe', 'Antoine', 350)
print ('O nome do livro é:',pequeno_principe.titulo)
print ('O nome do autor é:', pequeno_principe.autor)
print ('Quantidade de páginas:',pequeno_principe.num_paginas)

#Exercicio 2

class Retangulo:

    def __init__(self, lado_a,lado_b):
        self.ladoa=lado_a
        self.ladob=lado_b
        self.calcular_area=lado_a*lado_b
        self.calcular_perimetro=lado_a+lado_b

comprimento=float(input('Informe o comprimento do retangulo:'))
largura=float(input('Informe a largura do retangulo:'))
retangulo=Retangulo(comprimento,largura)
print('àrea do retângulo:', retangulo.calcular_area)
print('Perimetro do retângulo:', retangulo.calcular_perimetro)


#Exercicio 3

class Televisao:

    def __init__ (self, canal, volume):
        self.canal=canal
        self.volume=volume

    def aumentar_volume(self):
        self.volume+=1

    def diminuir_volume(self):
        self.volume-=1

    def alterar_canal (self, canal):
        self.canal=canal

tv=Televisao(None,0)
tv.alterar_canal(12)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('A TV está no canal:', tv.canal)
print('A TV está no volume:', tv.volume)

#Exercicio 4

class Aluno:

    def __init__ (self, nome, tempo_sem_dormir):
        self.nome=nome
        self.tempo=tempo_sem_dormir

    def estudar(self, horas_estudo):
        self.tempo+=horas_estudo

    def dormir(self, horas_sono):
        self.tempo-=horas_sono

aluno1 = Aluno('Renato',0)
aluno2 = Aluno('Pedro',0)
aluno1.estudar(3)
aluno1.dormir(2)
aluno1.estudar(4)
aluno1.dormir(2)
aluno2.estudar(7)
aluno2.dormir(5)
aluno2.estudar(4)

print('O aluno', aluno1.nome, 'esta', aluno1.tempo,'horas sem dormir')

print('O aluno', aluno2.nome, 'esta', aluno2.tempo,'horas sem dormir')







    
