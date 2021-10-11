class Produto:
    def __init__(self,descricao,preco):
        self.__descricao = descricao
        self.__preco = preco
    
    def get_descricao(self):
            return self.__descricao

    def get_preco(self):
            return self.__preco

    def set_descricao(self,descricao):
            self.__descricao = descricao

    def set_preco(self,preco):
            self.__preco = preco

class OrdemServico:
    def __init__(self):
        self.__lista_produtos=[]
    
    def adicionar_produto(self,item):
            self.__lista_produtos=self.__lista_produtos.append(item)

    def get_total(self):
            total=0
            for prod in self.__lista_produtos:
                total+=prod.get_preco()
            return total


def programa_principal():
	prod1 = Produto('Cafe', 7.50)
	prod2 = Produto('Arroz', 4.25)
	prod3 = Produto('Alface', 2.90)
	ordem = OrdemServico()
	ordem.adicionar_produto(prod1)
	ordem.adicionar_produto(prod2)
	ordem.adicionar_produto(prod3)
	total = ordem.get_total()
	print('Total:', total)

try:
	programa_principal()
except:
	print('Erro no programa principal.')
