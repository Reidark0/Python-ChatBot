import func
from func import dia_por_extenso


print('Bem-vindo à Barbearia 90S!')
print('Qual é o seu nome?')
nome = (input())
print(f'Olá {nome}')
print(('Escolha uma opção para começar:' ))
selecione = '0'
while selecione == '0':       # Loop para poder vooltar a esse menu
    print('1 - Serviços\n'    
          '2 - Sobre nós\n'
          '3 - Dúvidas\n'
          '4 - Cursos\n'
          '0 - Sair\n')
    selecione = input()
    # Sair do programa
    if selecione == '0':
        print('Deseja realmente sair?\n'
              '1 - Sim\n'
              '0 - Não\n')
        saida = input()
        if saida == '1':
            print(f'Tudo bem {nome}. nos avise se tiver algo com que possamos te ajudar!')
            exit()
        elif saida == '0':
            print(f'{nome} escolha uma das opções abaixo:')
            continue
    # Serviços
    elif selecione == '1':
        while selecione == '1':       # Loop para voltar a esse menu secundário
            print('Qual serviço você gostaria?\n'
                  '1 - Corte de cabelo\n'
                  '2 - Barba e cabelo\n'
                  '3 - Completo: Barba, cabelo, bigode e sobrancelha\n'
                  '0 - Voltar ao menu anterior\n'
                  'Digite o número do serviço:\n ')
            resposta = input()
            if resposta == '0':
                selecione = '0'
                print(f'{nome} escolha uma das opções abaixo:')
                break
            elif resposta == '1':
                print('Escolha uma data para reservar:\n'
                        '1 terça-feira\n'
                        '2 quarta-feira\n'
                        '3 quinta-feira\n'
                        '4 sexta-feira\n'
                        '5 sábado\n')
                dia = int(input())
                dia_extenso = dia_por_extenso(dia)
                print('Qual horário gostaria de agendar?\n ')
                hora = input()
                print(f'Você está agendado para: {dia_extenso} às {hora}')
                func.retornopequeno()
                selecione = '0'
                print(f'{nome} escolha uma das opções abaixo:')
                break
    # Sobre nós
    elif selecione == '2':
        while selecione == '2':
            print(f'Que bom saber que você tem interesse em nós {nome}!\n'
                  'Oque você quer saber?\n'
                  '1 - Membros da equipe\n'
                  '2 - Fundação da barbearia\n'
                  '3 - Missão e Visão\n'
                  '0 - Voltar ao menu anterior\n')
            resposta = input()
            if resposta == '0':
                print(f'{nome} escolha uma das opções abaixo:')
                selecione = '0'
                break
            while resposta != '0':
                if resposta == '1':
                    print('Somos 5 integrantes.\n'
                          'Alex\n'
                          'Arthur\n'
                          'Daniel\n'
                          'Matheus\n'
                          'Rafael')
                    func.retornopequeno()
                    break
                elif resposta == '2':
                    print('A nossa barbearia surgiu em decorrencia de um trabalho do curso '
                          'da resilia que nós inspirou a criar essa barbearia, que apesar das dores de cabeça '
                          'iniciais conseguimos crescer e estarmos onde estamos.')
                    func.retornopequeno()
                    break
                elif resposta == '3':
                    print('A nossa missão é deixar o mundo mais bonito e levar mais confiança para as pessoas '
                          'que necessitem de um up na auto estima e na aparencia\n'
                          'A nossa Visão é ser a maior barbearia do País em 5 anos e espalhar a cultura '
                          'do bom corte de cabelo pelo mundo inteiro.')
                    func.retornopequeno()
                    break
    # Dúvidas
    elif selecione == '3':
        while selecione == '3':
            print('Sobre qual tópico você tem dúvidas?\n'
                  '1 - Horário de funcionamento.\n'
                  '2 - Localização.\n'
                  '3 - Formas de pagamento\n'
                  '4 - Outras dúvidas\n'
                  '0 - Voltar ao menu anterior\n')
            resposta = input()
            if resposta == '0':
                print(f'{nome} escolha uma das opções abaixo:')
                selecione = '0'
                break
            while resposta != '0':
                if resposta == '1':
                    print('Funcionamos das 08:00 as 22:00 de Segunda a Sexta-Feira')
                    func.retornopequeno()
                    break
                elif resposta == '2':
                    print('Estamos localizados na rua Ifood, n50, Resilia, 50500-500')
                    func.retornopequeno()
                    break
                elif resposta == '3':
                    print('Crédito, Débito, Dinheiro e PIX')
                    func.retornopequeno()
                    break
                elif resposta == '4':
                    print('Para sanar outras dúvidas, entre em contato conosco pelo número: (50)95050-5050')
                    func.retornopequeno()
                    break
    # Cursos
    elif selecione == '4':
        while selecione == '4':
            print('Qual curso você tem interesse?\n'
                  '1 - Especialização em Cabelos Crespos e Cacheados;\n'
                  '2 - Hair Design;\n'
                  '0 - Voltar ao menu anterior\n')
            resposta= input()
            if resposta == '0':
                print(f'{nome} escolha uma das opções abaixo:')
                selecione = '0'
                break
            while resposta != '0':
                if resposta == '1':
                    print('Aprenda técnicas exclusivas para cortar cabelos crespos e cacheados'
                          ' no nosso curso especializado!\n Profissionais qualificados irão '
                          'ensinar desde cortes básicos até os mais elaborados. Torne-se um '
                          'especialista em cabelos crespos e cacheados e comece a transformar '
                          'a vida de muitas pessoas com seus cortes incríveis.\n'
                          'Matricule-se agora mesmo!')
                    resposta = func.retornopequeno()
                    break       
                elif resposta == '2':
                    print('O nosso curso de Hair Design é a escolha perfeita para quem deseja '
                          'se tornar um especialista em cabelos.\n'
                          'Com técnicas exclusivas e profissionais altamente capacitados, '
                          'você aprenderá desde cortes modernos até penteados elaborados, '
                          'garantindo resultados incríveis e duradouros.\n'
                          'Não perca mais tempo e matricule-se agora em nosso curso de'
                          'Hair Design para se tornar um profissional de excelência!')
                    resposta = func.retornopequeno()
                    break
