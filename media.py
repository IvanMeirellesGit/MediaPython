def qtdNota():
    QtdNum = 0
    while QtdNum <= 0:
        QtdNum = int(input(f'Agora {nome}, me diga quantas notas deseja inserir para calcular a média: '))
        if QtdNum <= 0:
            print('Número inválido. Por favor, insira um valor maior que zero.')
    return QtdNum

def insertNota(QtdNum):
    ListNum = []
    for i in range(QtdNum):
        num = float(input(f'Digite a {i + 1} Nota: '))
        ListNum.append(num)
    return ListNum

def calculaMedia(ListNum, aluno):
    if len(ListNum) > 0:
        media = sum(ListNum) / len(ListNum)
        print(f'A média do aluno {aluno} é {media}')
    else:
        print('Lista de Notas vazia. Não é possivel calcular a média')
    return media

def calculaMediarec(ListNum, media, aluno):
    if len(ListNum) > 0:
        media = (sum(ListNum) / len(ListNum)) + media
        print(f'A média do aluno {aluno} é {media}')
    else:
        print('Lista de Notas vazia. Não é possivel calcular a média')
    return media
def estadoBimestre(media, aluno):
    estado = 0
    if media >= 7:
        print(f'Aluno {aluno} foi aprovado!')
        estado = 1
    elif media < 7 and media >= 5:
        print(f'Aluno {aluno} está de recuperação!')
        estado = 2
    else:
        print(f'Aluno {aluno} reprovado!')
        estado = 3
    return estado

def notaRecupera(estadoBim, media, aluno):
    if estadoBim == 2:
        switch = int(input('Deseja acrescentar nota de recuperação? 0 para NÃO 1 para SIM: '))

        match switch:
            case 0:
                print(f'Aluno {aluno} reprovado!')
            case 1:
                QtdNota = qtdNota()

                recAluno = insertNota(QtdNota)

                mediarec = calculaMediarec(recAluno, media, aluno)
                print(mediarec)
        estadoBimestre(mediarec, aluno)

print('=' * 80)
print('Bem vindo ao meu programa de cálculo de médias de um aluno')
print('=' * 80)

nome = input('\nPrimeiro me diga seu nome: ')
aluno = input('Agora me diga o nome do aluno para lançar as notas: ')
print('=' * 80)

QtdNum = qtdNota()

notasAluno = insertNota(QtdNum)

media = calculaMedia(notasAluno, aluno)

estadoBim = estadoBimestre(media, aluno)

notaRecupera(estadoBim, media, aluno)