# Vamos iniciar o Trabalho aqui.
# Tomem cuidado para mexer só na parte de vocês para não quebrar o programa
# Se não forem mexer sozinhos usem branchs para codar e depois façam o merge.
# Não economizem nos commits, pode fazer vários sem medo.
# 
# Nos Commits escrevam no início:
# "feature: " ao adicionar coisas
# "edit: " se editarem alguma coisa, sem adicionar nada
# "fix: se consetarem algum problema no código "
# "Style: " se a mudança for na aparencia do código
# e descrevam oque você fez.
# 
# Lembrem de Dar git pull antes de começar a codar pra editar o código mais recente

print(f'Bem-vindo à Barbearia 90S')
nome = (input(f'Qual seu nome? '))
print(f'Olá {nome}')

servicos = 1
agendamento = 2
duvidas = 3
sair = 4

print(f'1. Serviços')
print(f'2. Agendamento')
print(f'3. Dúvidas')
print(f'4. Sair')

selecione = (int(input(f'Escolha uma opção para começar:' )))

if (selecione == 1):
       resposta = int((input(f'Qual serviço você gostaria?\n'
                            f'{1} Corte de cabelo.\n'
                            f'{2} Barba e cabelo.\n'
                            f'{3} Completo: Barba, cabelo\n'
                            f'bigode e sobrancelha\n'
                            f'Digite o número do serviço: ')))
       print(f'Você escolheu o serviço', resposta)

       confirmacao = input(f'Agendar? (sim/não): ')

       while (confirmacao == 'sim') or (confirmacao == 'nao'):
              if confirmacao == 'sim':
                dia = input(f'{1} terça-feira\n'
                            f'{2} quarta-feira\n'
                            f'{3} quinta-feira\n'
                            f'{4} sexta-feira\n'
                            f'{5} sábado\n'
                            f'Qual dia gostaria de agendar?')
                hora = input(f'Qual horário gostaria de agendar? ')
                print(f'Você está agendado para: ', dia, hora)
                break
if (selecione == 3):
       resposta2 = input(f'O que você gostaria de saber?\n'
                         f'{1} Dia e horário de funcionamento\n'
                         f'{2} Localização\n'
                         f'{3} Formas de pagamento\n'
                         f'Selecione uma opção:')
if resposta2 == 1: 
       print(f'Funcionamos de segunda à sexta das 9h às 21h')
elif resposta2 == 2:
       print(f'Estamos localizados na Rua das Palmeiras, 33')

