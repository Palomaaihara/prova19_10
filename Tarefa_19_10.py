# importa csv
import csv


#CADASTRAR PESSOAS
def cadastrar_pessoa(Pessoas,nome,email,telefone):
    pessoa = {
        'NOME': nome,
        'EMAIL': email,
        "TELEFONE": telefone
    }
    pessoas.apppend(pessoa)
pessoas = []
with open('pessoas.csv', mode='w', newline='') as pessoas_csv:
        writer = csv.writer(pessoas_csv)
        writer.writerow(["ID","Nome", "e-Mail", "Telefone"])
        for pessoa in pessoas:
            writer.writerow([pessoa,pessoa['NOME'], pessoa['EMAIL'], pessoa['TELEFONE']])

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
    for i,cad_pessoa in enumerate(pessoas):
	    print("Número de cadastro da pessoa:",i)
        print("NOME:", cad_pessoa['NOME'])
        print("NUMERO:", cad_pessoa['NUMERO'])
        print("EMAIL:", cad_pessoa['EMAIL'])
    
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
        with open('pessoas.cvs', 'r') as pessoas_cvs:
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
def deletar_emprestimo(emprestimo_csv, pessoas):
    emprestimo_para_remover = []

    # Encontra o índice das pessoas a serem removidas na lista
    for i, emprestimo in enumerate(emprestimos):
        if emprestimo['NOME'] == pesquisa:
            emprestimo_para_remover.append(i)

    if not emprestimo_para_remover:
        print("Nome não encontrado na lista!")
    else:
        # Abre o arquivo CSV para leitura e escrita
        with open(emprestimo_csv, 'r') as file:
            reader = csv.DictReader(file)
            emprestimo_no_arquivo = list(reader)

        # Remove as pessoas da lista em memória
        for i in reversed(emprestimo_para_remover):
            emprestimo.pop(i)

        # Abre o arquivo CSV para escrita e escreve as pessoas restantes
        with open(emprestimo_csv, 'w', newline='') as file:
            fieldnames = emprestimo_no_arquivo[0].keys()  # Obtém os cabeçalhos do CSV do arquivo
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(emprestimo_no_arquivo)  # Escreve as pessoas restantes

        print("Pessoa(s) removida(s) com sucesso!")
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
 		imp_pessoa(pessoas)


            elif op == "4":
                print("----DELETAR PESSOA----")
                pesquisa = input("Digite o nome que deseja excluir: ")
                deletar_pessoa()


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



            elif op == "2":
                print("----IMPRIMIR LIVROS ----")




            elif op =="3":
                print("----ATUALIZAR LIVRO----")



            elif op == "4":
                print("----DELETAR LIVRO ----")



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
                print("----DELETAR PESSOA----")



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
