# Impressão de boas vindas ao cliente junto a coleta do primeiro dado "nome"
print('Bem-vindo à Barbearia 90S')
nome = (input('Qual seu nome? '))
print('Olá', nome)

# Menu que guardam as variáveis correspondentes aos serviços 
servicos = 1
agendamento = 2 # Esta parte será implementada de maneira direta após a escolha de "serviços"
     # Corrigir e retirar
duvidas = 3
sair = 4

print('1. Serviços')
print('2. Agendamento')
print('3. Dúvidas')
print('4. Sair')

# Coleta da opção para dar entrada no serviço 
selecione = (int(input(f'Escolha uma opção para começar:' )))

if (selecione == 1): # Ao entrar no menu, outra coleta da variável correspondente ao
       #serviço escolhido sguindo do agendamento, utilizando while para verificação das respostas seguindo a tabela verdade
       # - corrigir esta função -

       resposta = int((input(f'Qual serviço você gostaria?\n{1} Corte de cabelo.\n{2} Barba e cabelo.\n{3} Completo: Barba, cabelo\n bigode e sobrancelha\nDigite o número do serviço: ')))
       print(f'Você escolheu o serviço', resposta)
       
       confirmacao = input('Agendar? (sim/nao): ')
              
       while (confirmacao == 'sim') or (confirmacao == 'nao'):
            if confirmacao == 'sim':
                dia = input(f'{1} terça-feira\n{2} quarta-feira\n{3} quinta-feira\n{4} sexta-feira\n{5} sábado\n Qual dia gostaria de agendar?')
                hora = input('Qual horário gostaria de agendar? ')
                print(f'Você está agendado para: ', dia, hora)
            else:
                break
                
       ## Este menu foi criado apenas para teste de verificação de entrada 
'''if (selecione == 3):
       resposta2 = input(f'O que você gostaria de saber?\n{1} Dia e horário de funcionamento\n{2} Localização\n{3} Formas de pagamento\n Selecione uma opção:')
if resposta2 == 1: 
       print('Funcionamos de segunda à sexta das 9h às 21h')
elif resposta2 == 2:
       print('Estamos localizados na Rua das Palmeiras, 33')'''