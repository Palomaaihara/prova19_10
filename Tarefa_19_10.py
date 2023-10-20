# importa csv
import csv


#CADASTRAR PESSOAS
with open('pessoas.csv', mode='w', newline='') as pessoas_csv:
        writer = csv.writer(pessoas_csv)
        writer.writerow(["ID","Nome", "e-Mail", "Telefone"])
        for pessoa in pessoas:
            writer.writerow([pessoa,pessoa['NOME'], pessoa['EMAIL'], pessoa['TELEFONE']])


#cadastra_livro

def cadastrar_livro(livros,titulo,autor,editora):
    livro = {
        'TITULO': titulo,
        'AUTOR': autor,
        'EDITORA': editora
    }
    livros.append(pessoa)
livros = []

with open('livros.csv', mode='w', newline='') as livros_csv:
        writer = csv.writer(livros_csv)
        writer.writerow(["Titulo", "Autor", "Editora"])
        for livro in livros:
            writer.writerow([livro['TITULO'], livro['AUTOR'], livro['EDITORA']])

print("MENU")
nome = str(input("Digite o nome: "))
email = str(input("Digite o email: "))
telefone = int(input("Ditegite o telefone: "))


#IMPRIMIR PESSOAS
def imp_pessoa(pessoas):
    for i,pessoa in enumerate(pessoas):
	    print("Número de cadastro da pessoa:",i)
        print("Nome:", pessoa['NOME'])
        print("Email:", pessoa['EMAIL'])
        print("Telefone:", pessoa['TELEFONE'])
    
with open('pessoas.csv', 'r', newline='') as pessoas_csv:
        linhas = csv.reader(pessoas_csv)
        for linha in linhas:
            print(linha[0], linha[1], linha[2])
#ATUALIZAR PESSOA

id = input("Digite o nome: ")

for pessoa in pessoas:
    if nome == pessoa['NOME']:
        numero = input("numero: ")
        mail = input("Email: ")
        with open('pessoas.cvs', 'r') as pessoas_csv:
            leitor = csv.reader(pessoas_csv)
            for linha in linhas:
                if linha == nome:

#DELETAR PESSOA
def deletar_pessoa(pessoas_csv, pessoas):
    pessoas_para_remover = []

    # Encontra o índice das pessoas a serem removidas na lista
    for i, pessoa in enumerate(pessoas):
        if pessoa['NOME'] == pesquisa:
            pessoas_para_remover.append(i)

    if not pessoas_para_remover:
        print("Nome não encontrado na lista!")
    else:
        # Abre o arquivo CSV para leitura e escrita
        with open(pessoas_csv, 'r') as file:
            reader = csv.DictReader(file)
            pessoas_no_arquivo = list(reader)

        # Remove as pessoas da lista em memória
        for i in reversed(pessoas_para_remover):
            pessoas.pop(i)

        # Abre o arquivo CSV para escrita e escreve as pessoas restantes
        with open(pessoas_csv, 'w', newline='') as file:
            fieldnames = pessoas_no_arquivo[0].keys()  # Obtém os cabeçalhos do CSV do arquivo
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(pessoas_no_arquivo)  # Escreve as pessoas restantes

        print("Pessoa(s) removida(s) com sucesso!")

#DELETAR EMPRESTIMO
def deletar_emprestimo(emprestimos_csv, emprestimo):
    emprestimo_para_remover = []

    
    for i, emprestimo in enumerate(emprestimos):
        if emprestimo['EMPRESTIMO'] == pesquisa:
            emprestimo_para_remover.append(i)

    if not emprestimo_para_remover:
        print("Emprestimo não encontrado na lista!")
    else:
        
        with open(emprestimos_csv, 'r') as file:
            reader = csv.DictReader(file)
            emprestimo_no_arquivo = list(reader)

        
        for i in reversed(emprestimo_para_remover):
            emprestimo.pop(i)

       
        with open(emprestimos_csv, 'w', newline='') as file:
            fieldnames = emprestimo_no_arquivo[0].keys()  
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(emprestimo_no_arquivo) 

        print("Emprestimo removido com sucesso!")
#DELETAR LIVRO
def deletar_livros(livros_csv, livros):
    pesquisa = input("Digite o livro que deseja excluir: ")
    livro_para_remover = []

    
    for i, livro in enumerate(livros):
        if livro['TITULO'] == pesquisa:
            livro_para_remover.append(i)

    if not livro_para_remover:
        print("Livro não encontrado na lista!")
    else:
        
        with open(livros_csv, 'r') as file:
            reader = csv.DictReader(file)
            livro_no_arquivo = list(reader)

    
        for i in reversed(livro_para_remover):
            livros.pop(i)

        
        with open(livro_pessoas_csv, 'w', newline='') as file:
            fieldnames = livro_no_arquivo[0].keys() 
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(livro_no_arquivo)  

        print("Livro removido com sucesso!")

#IMPRIMIR_REGISTRO

def imp_registro(emprestimos):
	for i,emprestimo in enumerate(emprestimos):
		print("Número do registro:",i)
		print("NOME:",emprestimo['PESSOA'])
		print("LIVRO:",emprestimo['LIVRO'])
		print("DATA DO EMPRESTIMO:",emprestimo['DATA_EMP'])
		print("DATA DE DEVOLUCAO",emprestimo['DATA_ENTREGA'])
          
#IMPRIMIR_ATRASADOS

def imp_atrasados(emprestimos,data_entrega,pessoa,livro):
	data = datetime.datetime.now()
	for i,emprestimo in enumerate(emprestimos):
		if data_entrega< data:
			print("Número do registro:",i)
			print("NOME:",emprestimo['PESSOA'])
			print("LIVRO:",emprestimo['LIVRO'])
			print("DATA DO EMPRESTIMO:",emprestimo['DATA_EMP'])
			print("DATA DE DEVOLUCAO:",emprestimo['DATA_ENTREGA'])

#menu
while True:
    print("------BIBLIOTECA------")
    print("    1 = PESSOAS       ")
    print("    2 = LIVROS        ")
    print("    3 = EMPRESTIMO    ")
    print("    4 = SAIR          ")
    print("----------------------")
    op = str(input("ESCOLHA UMA OPÇÃO:"))

    if op == "1":
        while True:
            print("------PESSOAS---------")
            print("    1 = CADASTRAR  ")
            print("    2 = IMPRIMIR   ")
            print("    3 = ATUALIZAR  ")
            print("    4 = DELETAR    ")
            print("    5 = ENCERRAR   ")
            print("----------------------")
            op = str(input("ESCOLHA UMA OPÇÃO:"))


            if op == "1":
                print("----CADASTRAR PESSOAS----")

            elif op == "2":
                print("----IMPRIMIR PESSOAS----")



            elif op =="3":
                print("----ATUALIZAR PESSOA----")
 		        imp_pessoa(pessoas_csv,pessoas)


            elif op == "4":
                print("----DELETAR PESSOA----")
                pesquisa = input("Digite o nome que deseja excluir: ")
                deletar_pessoa(pessoas_csv, pessoas)


            elif op == "5":
                break



            else: 
                print("-------------------")
                print("  OPÇÃO INVALIDA   ")
                print("-------------------") 


    elif op == "2":


         while True:
            print("------LIVRO-----------")
            print("    1 = CADASTRAR  ")
            print("    2 = IMPRIMIR   ")
            print("    3 = ATUALIZAR  ")
            print("    4 = DELETAR    ")
            print("    5 = ENCERRAR   ")
            print("----------------------")
            op = str(input("ESCOLHA UMA OPÇÃO:"))


            if op == "1":
                print("----CADASTRAR LIVRO ----")
                titulo = str(input("Digite o título do livro: "))
	    	    autor = str(input("Digite o nome do autor do livro: "))
	    	    editora = str(input("Digitebo nome da editora do livro: "))
                cadastrar_livro(livros,titulo,autor,editora)


            elif op == "2":
                print("----IMPRIMIR LIVROS ----")




            elif op =="3":
                print("----ATUALIZAR LIVRO----")



            elif op == "4":
                print("----DELETAR LIVRO ----")
                deletar_livros(livros_csv, livros)


            elif op ==  "5": 
                break    


            else: 



                print("-------------------")
                print("  OPÇÃO INVALIDA   ")
                print("-------------------") 



    elif op =="3":



        while True:
            print("------EMRPESTIMO------")
            print("    1 = CRIAR   ")
            print("    2 = IMPRIMIR    ")
            print("    3 = EMPRESTIMOS ATRASSADO ")
            print("    4 = ATUALIZAR  ")
            print("    5 = DELETAR    ")
            print("    6 = ENCERRAR   ")
            print("----------------------")
            op = str(input("ESCOLHA UMA OPÇÃO:"))


            if op == "1":
                print("----CRIAR EMPRESTIMOS----")



            elif op == "2":
                print("----IMPRIMIR EMPRESTIMOS----")



            elif op == "3":
                print("----EMPRESTIMOS ATRASSADO----")



            elif op == "4":
                print("----ATUALIZAR EMPRESTIMOS----")



            elif op == "5":
                print("----DELETAR EMPRESTIMOS----")
                deletar_emprestimo(emprestimos_csv, emprestimo)



            elif op == "6":
                break



            else: 
                print("-------------------")
                print("  OPÇÃO INVALIDA   ")
                print("-------------------") 




    elif op == "4":
        break
    else: 
        print("-------------------")
        print("  OPÇÃO INVALIDA   ")
        print("-------------------") 
