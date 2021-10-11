def buscar(dicionario, matricula):
    try:
        if type(matricula) is not int:
            raise TypeError
        elif (matricula<99999) or (matricula>999999):
            raise ValueError
        else:
            return dicionario[matricula]
        
        
    except TypeError:
        print("O parâmetro matricula deve ser inteiro!")
    except ValueError:
        print("O numero de matricula deve ter 6 digitos!")
    except KeyError:
        print("Não existe aluno com este numero de matricula!")
    except:
        print("Um erro inesperado ocorreu!")
        


	dicionario = {123456: 'Joao', 202018: 'Maria', 202088:'Jose', 202015: 'Bia', 202010: 'Caio'}
	matricula = int(input("Informe a matrícula do aluno: "))
	nome_aluno = buscar(dicionario, matricula)
	if nome_aluno != None:
		print(nome_aluno)
programa_principal()
