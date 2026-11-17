# ChatBot de atendimento da clínica Dr. Saúde

LINHA = "=" * 40

opcoes_menu = [
    "Marcação de consultas",
    "Retirada de exames",
    "Retorno de consultas",
    "Cancelar consulta",
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
exames_em_analise = ["1003", "1004", "1006"]

# cada consulta fica salva como [nome, especialidade, horario]
consultas = []


def ler_numero(mensagem, maximo):
    # Repete a pergunta até a pessoa digitar um número de 0 a maximo
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit() and int(valor) <= maximo:
            return int(valor)
        print(f"Opção inválida. Digite um número de 0 a {maximo}.")


def buscar_consultas(nome):
    # Devolve as consultas marcadas no nome informado, sem diferenciar maiúsculas
    encontradas = []
    for consulta in consultas:
        if consulta[0].lower() == nome.lower():
            encontradas.append(consulta)
    return encontradas


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
        print("[ 0 ] - Voltar")

        escolha = ler_numero("Escolha a especialidade: ", len(especialidades))

        if escolha != 0:
            especialidade = especialidades[escolha - 1]
            livres = horarios[escolha - 1]

            if len(livres) == 0:
                print(f"\nNão há horários livres para {especialidade}.")
            else:
                print(f"\nHorários livres para {especialidade}:")
                for i in range(len(livres)):
                    print(f"[ {i + 1} ] - {livres[i]}")
                print("[ 0 ] - Voltar")

                escolha_hora = ler_numero("Escolha o horário: ", len(livres))

                if escolha_hora != 0:
                    hora = livres[escolha_hora - 1]

                    nome = input("Digite seu nome completo: ").strip()
                    while not nome.replace(" ", "").isalpha():
                        print("Nome inválido. Use apenas letras.")
                        nome = input("Digite seu nome completo: ").strip()
                    nome = nome.title()

                    confirma = input(f"\nConfirmar {especialidade}, às {hora}, para {nome}? (s/n): ").strip().lower()

                    if confirma in ["s", "sim"]:
                        consultas.append([nome, especialidade, hora])
                        livres.remove(hora)
                        print(f"\nConsulta marcada: {especialidade}, às {hora}, para {nome}.")
                    else:
                        print("\nMarcação cancelada.")

    elif opcao == "2":
        protocolo = input("\nDigite o número do protocolo do exame: ").strip()

        if protocolo in exames_prontos:
            print("\nSeu exame já está pronto.")
            print("Pode retirar na recepção, de segunda a sexta, das 7h às 17h, com um documento com foto.")
        elif protocolo in exames_em_analise:
            print("\nSeu exame ainda está em análise. Tente de novo amanhã.")
        else:
            print("\nProtocolo não encontrado. Confira o número no seu comprovante.")

    elif opcao == "3":
        nome = input("\nDigite seu nome completo: ").strip()
        encontradas = buscar_consultas(nome)

        if len(encontradas) == 0:
            print("\nNão encontramos consultas nesse nome.")
        else:
            print("\nSuas consultas:")
            for consulta in encontradas:
                print(f"- {consulta[1]}, às {consulta[2]}")
            print("O retorno é gratuito se for feito em até 30 dias. É só procurar a recepção.")

    elif opcao == "4":
        nome = input("\nDigite seu nome completo: ").strip()
        encontradas = buscar_consultas(nome)

        if len(encontradas) == 0:
            print("\nNão encontramos consultas nesse nome.")
        else:
            print("\nSuas consultas:")
            for i in range(len(encontradas)):
                print(f"[ {i + 1} ] - {encontradas[i][1]}, às {encontradas[i][2]}")
            print("[ 0 ] - Voltar")

            escolha = ler_numero("Qual consulta deseja cancelar? ", len(encontradas))

            if escolha != 0:
                consulta = encontradas[escolha - 1]
                confirma = input(f"\nCancelar {consulta[1]}, às {consulta[2]}? (s/n): ").strip().lower()

                if confirma in ["s", "sim"]:
                    consultas.remove(consulta)
                    # o horário volta para a lista de livres da especialidade
                    pos = especialidades.index(consulta[1])
                    horarios[pos].append(consulta[2])
                    horarios[pos].sort()
                    print(f"\nConsulta cancelada. O horário das {consulta[2]} está livre de novo.")
                else:
                    print("\nA consulta foi mantida.")

    elif opcao == "5":
        print("\nLigue para (00) 0000-0000, de segunda a sexta, das 7h às 19h.")

    elif opcao == "6":
        print("\nObrigado por utilizar o Dr. Saúde. Até logo!")
        continuar = False

    else:
        print(f"\nOpção inválida! Por favor, digite um número de 1 a {len(opcoes_menu)}.")

    if continuar:
        input("\nAperte Enter para voltar ao menu...")

input("\nPressione Enter para fechar...")

input("\nPressione Enter para fechar...")

