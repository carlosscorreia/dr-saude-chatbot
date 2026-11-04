#Dar inicio a criação do ChatBot
#Nome da empresa : Dr. Saúde -
#Opções de atendimento:
#1 - Marcação de consultas
#2 - Retirada de exames
#3 - Retorno de consultas
#4 - Falar com o atendente
#5 - Sair

print("=" * 35) #Apenas para enfeitar
print("     Bem-vindo ao Dr. Saúde!") #Mensagem de boas vindas
print("=" * 35) #Apenas para enfeitar
print("Escolha uma das opções abaixo:\n") #Apresentação das opções
print("[ 1 ] - Marcação de consultas") 
print("[ 2 ] - Retirada de exames") 
print("[ 3 ] - Retorno de consultas")
print("[ 4 ] - Falar com o atendente")
print("[ 5 ] - Sair")
print("=" * 35)

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print("\nVocê escolheu: Marcação de consultas. Aguarde um instante...")
elif opcao == "2":
    print("\nVocê escolheu: Retirada de exames. Por favor, tenha seu protocolo em mãos.")
elif opcao == "3":
    print("\nVocê escolheu: Retorno de consultas. Verificando datas disponíveis...")
elif opcao == "4":
    print("\nVocê escolheu: Falar com o atendente. Transferindo para um atendente...")
elif opcao == "5":
    print("\nObrigado por utilizar o Dr. Saúde. Até logo!")
else:
    print("\nOpção inválida! Por favor, digite um número de 1 a 5.")
