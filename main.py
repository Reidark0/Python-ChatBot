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


# Parte do Matheus -------------
import func
from func import dia_por_extenso

print(f'Bem-vindo à Barbearia 90S')
nome = (input(f'Qual seu nome? '))
print(f'Olá {nome}')
selecione = 0
while selecione == 0:
    print(f'1. Serviços')
    print(f'2. Sobre nós')
    print(f'3. Dúvidas')
    print(f'0. Sair')
    selecione = (int(input(f'Escolha uma opção para começar:' )))
    if (selecione == 1):
        resposta = int((input(f'Qual serviço você gostaria?\n'
                                f'{1} Corte de cabelo.\n'
                                f'{2} Barba e cabelo.\n'
                                f'{3} Completo: Barba, cabelo\n'
                                f'bigode e sobrancelha\n'
                                f'Digite o número do serviço: ')))
        print(f'Você escolheu o serviço', resposta)
#fix by Daniel
        confirmacao = input(f'Agendar? (sim/não): ')
        while (confirmacao == 'sim') or (confirmacao == 'nao'):
            if confirmacao == 'sim':
                dia = int(input(f'{1} terça-feira\n'
                                f'{2} quarta-feira\n'
                                f'{3} quinta-feira\n'
                                f'{4} sexta-feira\n'
                                f'{5} sábado\n'
                                f'Qual dia gostaria de agendar?'))
                dia_extenso = dia_por_extenso(dia)
                hora = input(f'Qual horário gostaria de agendar? ')
                print(f'Você está agendado para: {dia_extenso} às {hora}')
                break

    # Parte do Alex --------------------------
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
    # Parte do Rafael ---------------------
    if selecione == 2:
        while selecione == 2:
            print(f'Que bom saber que você tem interesse em nós!\n'
                  f'Oque você quer saber?\n')
            sobre1 = int(input(f'1 - Membros da equipe\n'
                               f'2 - Fundação da barbearia\n'
                               f'3 - Missão e Visão\n'
                               f'0 - Voltar ao menu anterior\n'))
            if sobre1 == 0:           # Para zerar a escolha inicial
                    print("Escolha uma das opções: ")
                    break
            while sobre1 != 0:
                if sobre1 == 1:
                    print(f'Somos 5 integrantes.\n'
                        f'Alex\n'
                        f'Arthur\n'
                        f'Daniel\n'
                        f'Matheus\n'
                        f'Rafael')
                    sobre1 = func.retornopequeno()
                    break
                elif sobre1 == 2:
                    print(f'A nossa barbearia surgiu em decorrencia de um trabalho do curso '
                          f'da resilia que nós inspirou a criar essa barbearia, que apesar das dores de cabeça '
                          f'iniciais conseguimos crescer e estarmos onde estamos.')
                    sobre1 = func.retornopequeno()
                    break
                elif sobre1 == 3:
                    print(f'A nossa missão é deixar o mundo mais bonito e levar mais confiança para as pessoas '
                          f'que necessitem de um up na auto estima e na aparencia\n'
                          f'A nossa Visão é ser a maior barbearia do País em 5 anos e espalhar a cultura '
                          f'do bom corte de cabelo pelo mundo inteiro.')
                    sobre1 = func.retornopequeno()
                    break
    if selecione == 0:
        print('Tudo bem. nos avise se tiver algo com que possamos te ajudar!')