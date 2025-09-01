# Lista global para armazenar os alunos
Alunos = []

contadores_matricula = {
    "GEC": 0,  # Engenharia de Computação
    "GES": 0,  # Engenharia de Software
    "GEA": 0,  # Engenharia de Automação
    "GEP": 0,  # Engenharia de Produção
    "GEE": 0   # Engenharia Elétrica
}

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o E-mail do aluno: ")

    # Garante que o usuário digite um curso válido
    while True:
        curso = input("Digite o curso do aluno (GEC, GES, GEA, GEP, GEE): ").upper()
        if curso in contadores_matricula:
            break
        else:
            print("Curso inválido. Tente novamente.")

    # Acessa e incrementa o contador global para o curso
    contadores_matricula[curso] += 1
    
    # Concatena a abreviação do curso com o novo contador para a matrícula
    matricula = f"{curso}{contadores_matricula[curso]}"
    
    # Adiciona a matrícula ao dicionário do aluno
    Alunos.append({"nome": nome, "email": email, "curso": curso, "mat": matricula})
    print(f"Aluno {nome} cadastrado com sucesso!")


def listar_alunos():
    if not Alunos:
        print("Não foram cadastrados alunos")
    else:
        for aluno in Alunos:
            print(f"Matrícula: {aluno['mat']}, Nome: {aluno['nome']}, Email: {aluno['email']}, Curso: {aluno['curso']}")


def atualizar_aluno():
    nome = input("Digite o nome do aluno para atualizar os dados: ")
    for aluno in Alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo email: ")
            aluno["curso"] = input("Digite o novo curso: ")
            return
    print("Aluno não encontrado")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in Alunos:
        if aluno["nome"] == nome:
            Alunos.remove(aluno)
            print("Aluno removido com sucesso")
            return
    print("Aluno não encontrado")

def main():
    flag = True
    while flag:
        print("\nOpção 1 - Cadastrar aluno")
        print("Opção 2 - Listar aluno")
        print("Opção 3 - Atualiza aluno")
        print("Opção 4 - Remover aluno")
        print("Opção 5 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            print("Saindo...")
            flag = False
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()