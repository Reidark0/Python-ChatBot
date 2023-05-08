import func
from func import dia_por_extenso

print(f'Bem-vindo à Barbearia 90S')
nome = (input(f'Qual seu nome? '))
print(f'Olá {nome}')
selecione = 0
print((f'Escolha uma opção para começar:' ))
while selecione == 0:       # Loop para poder vooltar a esse menu
    print(f'1. Serviços\n'    
          f'2. Sobre nós\n'
          f'3. Dúvidas\n'
          f'4. Cursos\n'
          f'0. Sair\n')
    selecione = (int(input()))
    # Sair do programa
    if selecione == 0:
        saida = input('Deseja realmente sair?'
                       f'1 - Sim\n'
                       f'0 - Não')
        if saida == '1':
            print('Tudo bem. nos avise se tiver algo com que possamos te ajudar!')
            exit()
        elif saida == '0':
            continue
    # Serviços
    elif (selecione == 1):
        while selecione == 1:       # Loop para voltar a esse menu secundário
            resposta = int((input(f'Qual serviço você gostaria?\n'
                                    f'1 Corte de cabelo.\n'
                                    f'2 Barba e cabelo.\n'
                                    f'3 Completo: Barba, cabelo, bigode e sobrancelha\n'
                                    f'0 Voltar.\n'
                                    f'Digite o número do serviço: ')))
            print(f'Você escolheu o serviço', resposta)
            if resposta == 0:
                selecione = 0 
                break
            confirmacao = input(f'Agendar?\n'
                                f'1 - Sim\n'
                                f'0 - Não')
            while (confirmacao == '1') or (confirmacao == '0'):
                if confirmacao == '1':
                    dia = int(input(f'1 terça-feira\n'
                                    f'2 quarta-feira\n'
                                    f'3 quinta-feira\n'
                                    f'4 sexta-feira\n'
                                    f'5 sábado\n'
                                    f'Qual dia gostaria de agendar?'))
                    dia_extenso = dia_por_extenso(dia)
                    hora = input(f'Qual horário gostaria de agendar? ')
                    print(f'Você está agendado para: {dia_extenso} às {hora}')
                    func.retornopequeno()
                    break
    # Sobre nós
    elif selecione == 2:
        while selecione == 2:
            print(f'Que bom saber que você tem interesse em nós!\n'
                  f'Oque você quer saber?\n')
            sobre1 = int(input(f'1 - Membros da equipe\n'
                               f'2 - Fundação da barbearia\n'
                               f'3 - Missão e Visão\n'
                               f'0 - Voltar ao menu anterior\n'))
            if sobre1 == 0:           # Para zerar a escolha inicial
                    print("Escolha uma das opções: ")
                    selecione = 0
                    break
            while sobre1 != 0:
                if sobre1 == 1:
                    print(f'Somos 5 integrantes.\n'
                        f'Alex\n'
                        f'Arthur\n'
                        f'Daniel\n'
                        f'Matheus\n'
                        f'Rafael')
                    func.retornopequeno()
                    break
                elif sobre1 == 2:
                    print(f'A nossa barbearia surgiu em decorrencia de um trabalho do curso '
                          f'da resilia que nós inspirou a criar essa barbearia, que apesar das dores de cabeça '
                          f'iniciais conseguimos crescer e estarmos onde estamos.')
                    func.retornopequeno()
                    break
                elif sobre1 == 3:
                    print(f'A nossa missão é deixar o mundo mais bonito e levar mais confiança para as pessoas '
                          f'que necessitem de um up na auto estima e na aparencia\n'
                          f'A nossa Visão é ser a maior barbearia do País em 5 anos e espalhar a cultura '
                          f'do bom corte de cabelo pelo mundo inteiro.')
                    func.retornopequeno()
                    break
    # Dúvidas
    elif selecione == 3:
        while selecione == 3:
            resposta = int(input(
                '\n1. Horário de funcionamento.\n'
                '2. Localização.\n'
                '3. Formas de pagamento\n'
                '4. Outras dúvidas\n'
                '0. Sair\n\n'
                'Escolha uma opção para prosseguir: '))
            while resposta != 0:
                if resposta == 1:
                    print("\nFuncionamos das 08:00 as 22:00!\n"
                        "Segunda a Sexta-Feira ;)\n")
                    func.retornopequeno
                    break
                elif resposta == 2:
                    print("\nEstamos localizados na rua Ifood, n50, Resilia, 50500-500\n\n")
                    func.retornopequeno
                    break
                elif resposta == 3:
                    print("\nCrédito, Débito, Dinheiro e PIX\n\n")
                    func.retornopequeno
                    break
                elif resposta == 4:
                    print("\nPara sanar outras dúvidas, entre em contato conosco pelo número: (50)95050-5050\n\n")
                    func.retornopequeno
                    break
    # Cursos
    elif selecione==4:
        while selecione == 4:
            print(f'Qual curso você tem interesse?\n')
            cursos_= int(input(f'1 Especialização em Cabelos Crespos e Cacheados;\n'
                                f'2 Hair Design;\n'
                                f'0 Menu Anterior.\n'))
            if cursos_ == 0:           
                print("Opções: ")
                selecione = 0
                break
            while cursos_ != 0:
                if cursos_ == 1:
                    print(f'Aprenda técnicas exclusivas para cortar cabelos crespos e cacheados no nosso curso especializado!'
                        f'Profissionais qualificados irão ensinar desde cortes básicos até os mais elaborados. Torne-se um '
                        f'especialista em cabelos crespos e cacheados e comece a transformar a vida de muitas pessoas com seus cortes incríveis.' 
                        f'Matricule-se agora mesmo!')
                    cursos_ = func.retornopequeno()
                    break       
                elif cursos_ == 2:
                    print(f'O nosso curso de Hair Design é a escolha perfeita para quem deseja se tornar um especialista em cabelos.'
                        f'Com técnicas exclusivas e profissionais altamente capacitados, você aprenderá desde cortes modernos até penteados' 
                        f'elaborados, garantindo resultados incríveis e duradouros. Não perca mais tempo e matricule-se agora em nosso curso de Hair Design' 
                        f'para se tornar um profissional de excelência!')
                    cursos_ = func.retornopequeno()
                    break
