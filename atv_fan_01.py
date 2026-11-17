# ChatBot de atendimento da clínica Dr. Saúde

LINHA = "=" * 40

opcoes_menu = [
    "Marcação de consultas",
    "Retirada de exames",
    "Retorno de consultas",
    "Falar com o atendente",
    "Sair",
]

especialidades = ["Clínico Geral", "Cardiologia", "Pediatria", "Dermatologia"]

# horarios[i] guarda os horários livres de especialidades[i]
horarios = [
    ["08:00", "09:00", "10:00", "14:00"],
    ["08:30", "13:00", "15:30"],
    ["09:00", "11:00", "16:00"],
    ["10:30", "14:30"],
]

exames_prontos = ["1001", "1002", "1005", "1010"]

# cada consulta fica salva como [nome, especialidade, horario]
consultas = []

print(LINHA)
print("       Bem-vindo ao Dr. Saúde!")
print(LINHA)

continuar = True

while continuar:
    print("\nEscolha uma das opções abaixo:\n")
    for i in range(len(opcoes_menu)):
        print(f"[ {i + 1} ] - {opcoes_menu[i]}")
    print(LINHA)

    opcao = input("Digite o número da opção desejada: ").strip()

    if opcao == "1":
        print("\nMarcação de consultas\n")
        for i in range(len(especialidades)):
            print(f"[ {i + 1} ] - {especialidades[i]}")

        escolha = input("Escolha a especialidade: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(especialidades):
            pos = int(escolha) - 1
            especialidade = especialidades[pos]
            livres = horarios[pos]

            if len(livres) == 0:
                print(f"\nNão há horários livres para {especialidade}.")
            else:
                print(f"\nHorários livres para {especialidade}:")
                for i in range(len(livres)):
                    print(f"[ {i + 1} ] - {livres[i]}")

                escolha_hora = input("Escolha o horário: ").strip()

                if escolha_hora.isdigit() and 1 <= int(escolha_hora) <= len(livres):
                    hora = livres[int(escolha_hora) - 1]
                    nome = input("Digite seu nome completo: ").strip()

                    if nome == "":
                        print("\nNome não informado, a marcação foi cancelada.")
                    else:
                        consultas.append([nome, especialidade, hora])
                        livres.remove(hora)
                        print(f"\nConsulta marcada: {especialidade}, às {hora}, para {nome}.")
                else:
                    print("\nHorário inválido.")
        else:
            print("\nEspecialidade inválida.")

    elif opcao == "2":
        protocolo = input("\nDigite o número do protocolo do exame: ").strip()

        if protocolo in exames_prontos:
            print("\nSeu exame já está pronto.")
            print("Pode retirar na recepção, de segunda a sexta, das 7h às 17h, com um documento com foto.")
        elif protocolo.isdigit():
            print("\nSeu exame ainda não está pronto. Tente de novo amanhã.")
        else:
            print("\nProtocolo inválido. Digite só os números.")

    elif opcao == "3":
        nome = input("\nDigite seu nome completo: ").strip()

        encontradas = []
        for consulta in consultas:
            if consulta[0].lower() == nome.lower():
                encontradas.append(consulta)

        if len(encontradas) == 0:
            print("\nNão encontramos consultas nesse nome.")
        else:
            print("\nSuas consultas:")
            for consulta in encontradas:
                print(f"- {consulta[1]}, às {consulta[2]}")
            print("O retorno é gratuito se for feito em até 30 dias. É só procurar a recepção.")

    elif opcao == "4":
        print("\nLigue para (00) 0000-0000, de segunda a sexta, das 7h às 19h.")

    elif opcao == "5":
        print("\nObrigado por utilizar o Dr. Saúde. Até logo!")
        continuar = False

    else:
        print("\nOpção inválida! Por favor, digite um número de 1 a 5.")

    if continuar:
        input("\nAperte Enter para voltar ao menu...")
