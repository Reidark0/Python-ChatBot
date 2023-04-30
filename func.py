# Aqu pra criar as funções e chamar como biblioteca no main.py

# função para retornar pro sobre-nos ou terminar
def retornopequeno():
    resposta = input("gostaria de saber algo mais? y/n \n")
    if resposta == 'y':
        return
    elif resposta == 'n':
        print(f'Obrigado por entrar em contato conosco!\n'
              f'Volte sempre!')
        exit()
