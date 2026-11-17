# ChatBot de atendimento da clínica Dr. Saúde

LINHA = "=" * 40
CODIGO_ADMIN = "0110"

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

# cada consulta fica salva como [nome, especialidade, horario, situacao]
# situacao: "agendada", "realizada", "retorno", "retorno marcado" ou "retorno realizado"
consultas = []

# cada exame fica salvo como [protocolo, nome, situacao]
# situacao: "em análise" ou "pronto"
exames = []


def ler_numero(mensagem, maximo):
    # Repete a pergunta até a pessoa digitar um número de 0 a maximo
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit() and int(valor) <= maximo:
            return int(valor)
        print(f"Opção inválida. Digite um número de 0 a {maximo}.")


def ler_nome():
    # Repete a pergunta até o nome ter apenas letras e espaços
    nome = input("Digite o nome completo: ").strip()
    while not nome.replace(" ", "").isalpha():
        print("Nome inválido. Use apenas letras.")
        nome = input("Digite o nome completo: ").strip()
    return nome.title()


def buscar_consultas(nome):
    # Devolve as consultas marcadas no nome informado, sem diferenciar maiúsculas
    encontradas = []
    for consulta in consultas:
        if consulta[0].lower() == nome.lower():
            encontradas.append(consulta)
    return encontradas


def escolher_horario(pos):
    # Mostra os horários livres da especialidade e devolve o escolhido (ou None)
    livres = horarios[pos]
    if len(livres) == 0:
        print(f"\nNão há horários livres para {especialidades[pos]}.")
        return None

    print(f"\nHorários livres para {especialidades[pos]}:")
    for i in range(len(livres)):
        print(f"[ {i + 1} ] - {livres[i]}")
    print("[ 0 ] - Voltar")

    escolha = ler_numero("Escolha o horário: ", len(livres))
    if escolha == 0:
        return None
    return livres[escolha - 1]


def area_administrativa():
    opcoes_admin = [
        "Ver todas as consultas",
        "Registrar consulta realizada",
        "Ver todos os exames",
        "Cadastrar exame",
        "Liberar resultado de exame",
    ]

    while True:
        print(f"\n{LINHA}")
        print("        Área administrativa")
        print(LINHA)
        for i in range(len(opcoes_admin)):
            print(f"[ {i + 1} ] - {opcoes_admin[i]}")
        print("[ 0 ] - Sair da área administrativa")

        escolha = ler_numero("Escolha uma opção: ", len(opcoes_admin))

        if escolha == 0:
            return

        elif escolha == 1:
            if len(consultas) == 0:
                print("\nNenhuma consulta registrada.")
            else:
                print("\nTodas as consultas:")
                for consulta in consultas:
                    print(f"- {consulta[0]} | {consulta[1]} | {consulta[2]} | {consulta[3]}")

        elif escolha == 2:
            pendentes = []
            for consulta in consultas:
                if consulta[3] in ["agendada", "retorno"]:
                    pendentes.append(consulta)

            if len(pendentes) == 0:
                print("\nNão há consultas aguardando atendimento.")
            else:
                print("\nConsultas aguardando atendimento:")
                for i in range(len(pendentes)):
                    print(f"[ {i + 1} ] - {pendentes[i][0]} | {pendentes[i][1]} | {pendentes[i][2]}")
                print("[ 0 ] - Voltar")

                num = ler_numero("Qual consulta foi realizada? ", len(pendentes))
                if num != 0:
                    consulta = pendentes[num - 1]
                    if consulta[3] == "retorno":
                        consulta[3] = "retorno realizado"
                    else:
                        consulta[3] = "realizada"
                    print(f"\nAtendimento de {consulta[0]} registrado.")

        elif escolha == 3:
            if len(exames) == 0:
                print("\nNenhum exame cadastrado.")
            else:
                print("\nTodos os exames:")
                for exame in exames:
                    print(f"- Protocolo {exame[0]} | {exame[1]} | {exame[2]}")

        elif escolha == 4:
            print()
            nome = ler_nome()
            protocolo = str(1001 + len(exames))
            exames.append([protocolo, nome, "em análise"])
            print(f"\nProtocolo {protocolo} gerado para {nome}.")

        elif escolha == 5:
            em_analise = []
            for exame in exames:
                if exame[2] == "em análise":
                    em_analise.append(exame)

            if len(em_analise) == 0:
                print("\nNão há exames em análise.")
            else:
                print("\nExames em análise:")
                for i in range(len(em_analise)):
                    print(f"[ {i + 1} ] - Protocolo {em_analise[i][0]} | {em_analise[i][1]}")
                print("[ 0 ] - Voltar")

                num = ler_numero("Qual exame ficou pronto? ", len(em_analise))
                if num != 0:
                    em_analise[num - 1][2] = "pronto"
                    print(f"\nResultado do protocolo {em_analise[num - 1][0]} liberado.")

        input("\nAperte Enter para continuar...")


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
            hora = escolher_horario(escolha - 1)

            if hora is not None:
                nome = ler_nome()
                confirma = input(f"\nConfirmar {especialidade}, às {hora}, para {nome}? (s/n): ").strip().lower()

                if confirma in ["s", "sim"]:
                    consultas.append([nome, especialidade, hora, "agendada"])
                    horarios[escolha - 1].remove(hora)
                    print(f"\nConsulta marcada: {especialidade}, às {hora}, para {nome}.")
                else:
                    print("\nMarcação cancelada.")

    elif opcao == "2":
        protocolo = input("\nDigite o número do protocolo do exame: ").strip()

        encontrado = None
        for exame in exames:
            if exame[0] == protocolo:
                encontrado = exame

        if encontrado is None:
            print("\nProtocolo não encontrado. Confira o número no seu comprovante.")
        elif encontrado[2] == "pronto":
            print(f"\nO exame de {encontrado[1]} está pronto.")
            print("Pode retirar na recepção, de segunda a sexta, das 7h às 17h, com um documento com foto.")
        else:
            print(f"\nO exame de {encontrado[1]} ainda está em análise. Tente de novo amanhã.")

    elif opcao == "3":
        nome = input("\nDigite seu nome completo: ").strip()
        encontradas = buscar_consultas(nome)

        realizadas = []
        tem_retorno = False
        for consulta in encontradas:
            if consulta[3] == "realizada":
                realizadas.append(consulta)
            if consulta[3] == "retorno":
                tem_retorno = True

        if len(encontradas) == 0:
            print("\nNão encontramos consultas nesse nome.")
        elif len(realizadas) == 0 and tem_retorno:
            print("\nSeu retorno já está marcado. Para cancelar, use a opção 4.")
        elif len(realizadas) == 0:
            print("\nNenhuma consulta sua está liberada para retorno.")
            print("O retorno fica disponível depois que a consulta é realizada.")
        else:
            print("\nConsultas realizadas:")
            for i in range(len(realizadas)):
                print(f"[ {i + 1} ] - {realizadas[i][1]}, às {realizadas[i][2]}")
            print("[ 0 ] - Voltar")

            num = ler_numero("Para qual consulta deseja marcar o retorno? ", len(realizadas))

            if num != 0:
                original = realizadas[num - 1]
                pos = especialidades.index(original[1])
                hora = escolher_horario(pos)

                if hora is not None:
                    confirma = input(f"\nConfirmar retorno em {original[1]}, às {hora}? (s/n): ").strip().lower()

                    if confirma in ["s", "sim"]:
                        consultas.append([original[0], original[1], hora, "retorno"])
                        horarios[pos].remove(hora)
                        original[3] = "retorno marcado"
                        print(f"\nRetorno marcado: {original[1]}, às {hora}. O retorno é gratuito.")
                    else:
                        print("\nRetorno não marcado.")

    elif opcao == "4":
        nome = input("\nDigite seu nome completo: ").strip()

        ativas = []
        for consulta in buscar_consultas(nome):
            if consulta[3] in ["agendada", "retorno"]:
                ativas.append(consulta)

        if len(ativas) == 0:
            print("\nNão encontramos consultas agendadas nesse nome.")
        else:
            print("\nSuas consultas agendadas:")
            for i in range(len(ativas)):
                print(f"[ {i + 1} ] - {ativas[i][1]}, às {ativas[i][2]} ({ativas[i][3]})")
            print("[ 0 ] - Voltar")

            escolha = ler_numero("Qual consulta deseja cancelar? ", len(ativas))

            if escolha != 0:
                consulta = ativas[escolha - 1]
                confirma = input(f"\nCancelar {consulta[1]}, às {consulta[2]}? (s/n): ").strip().lower()

                if confirma in ["s", "sim"]:
                    consultas.remove(consulta)
                    # o horário volta para a lista de livres da especialidade
                    pos = especialidades.index(consulta[1])
                    horarios[pos].append(consulta[2])
                    horarios[pos].sort()

                    # se era um retorno, a consulta original volta a aceitar retorno
                    if consulta[3] == "retorno":
                        for outra in consultas:
                            if outra[0] == consulta[0] and outra[1] == consulta[1] and outra[3] == "retorno marcado":
                                outra[3] = "realizada"

                    print(f"\nConsulta cancelada. O horário das {consulta[2]} está livre de novo.")
                else:
                    print("\nA consulta foi mantida.")

    elif opcao == "5":
        print("\nLigue para (00) 0000-0000, de segunda a sexta, das 7h às 19h.")

    elif opcao == "6":
        print("\nObrigado por utilizar o Dr. Saúde. Até logo!")
        continuar = False

    elif opcao == CODIGO_ADMIN:
        area_administrativa()

    else:
        print(f"\nOpção inválida! Por favor, digite um número de 1 a {len(opcoes_menu)}.")

    if continuar:
        input("\nAperte Enter para voltar ao menu...")

input("\nPressione Enter para fechar...")
