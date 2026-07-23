import os

import subprocess


def limpa_a_tela():
    if os.name == 'nt':
        #nt, aqui, delimita o windows.
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])
        #Pra linux e Mac
    
        #Podia ter usado o "os.system('clear')", mas, se puder, evita o os.

def autenticacao():
    nome = 'João'
    senha = '12345'

    while True:
        nome_inserido = input('Insira o nome de usuário:\n')
        senha_inserida = input('Insira a senha:\n') 

        if not nome_inserido and not senha_inserida:
            continue

        if nome == nome_inserido and senha == senha_inserida:
            limpa_a_tela()
            print('\nSeja bem vindo!\n')
            break

        else:
            limpa_a_tela()
            print('Usuário e/ou senha incorretos. Tente novamente.')

def nome_do_programa():
    print('Bem vindo ao conjunto de teste de condicionais!\n')

def par_ou_impar():
    while True:
        numero_par_ou_impar = input('Insira um número inteiro, e o programa dirá se é par ou ímpar.\n')

        try:
            numero = int(numero_par_ou_impar)

            if numero % 2 == 0:
                print('O número é par.')

            else:
                print ('O número é ímpar.')

            continuar = input('Deseja tentar outro? y para sim, qualquer outra coisa para não.\n').strip().lower()
                #.strip tira espaços em branco, .lower faz com que o programa pegue Y como y

            if continuar == 'y':
                limpa_a_tela()
                continue

            else:
                limpa_a_tela()
                break

        except ValueError:
            limpa_a_tela()
            print ('Insira um número inteiro válido.\n')

def grupo_etario():
    while True:
        idade = input('Insira o número inteiro relativo à sua idade, em anos, e o programa o encaixará em um grupo etário.\n')
        try:
                numero = int(idade)
        
                if numero < 0:
                    print('Espere o nascimento e tente novamente.')

                elif 0 <= numero <= 12:
                    print ('\nGrupo etário: Criança (0 a 12 anos).\n')

                elif 13 <= numero <= 18:
                    print ('\nGrupo etário: Adolescente (13 a 18 anos).\n')

                else:
                    print ('\nGrupo etário: Adulto (acima de 18 anos).\n')
        
                continuar = input('Deseja tentar outro? y para sim, qualquer outra coisa para não.\n').strip().lower()
                #.strip tira espaços em branco, .lower faz com que o programa pegue Y como y
                                                
                if continuar == 'y':
                    limpa_a_tela()
                    continue
                                                
                else:
                    break
                    
        except ValueError:
            limpa_a_tela()
            print ('Insira um número inteiro válido.\n')

def plano_cartesiano():
    print('Bem vindo ao localizador de coordenadas do plano Cartesiano!')
    print('\nPara começar, insira as coordenadas a seguir:\n')
    while True:
        x = input('Insira um número relativo ao eixo das abscissas (x). Use o ponto como separador.\n')
        y = input('\nInsira um número relativo ao eixo das ordenadas (y). Use o ponto como separador.\n')

        try:
            x_inserido = float(x) 
            y_inserido = float(y)

            if x_inserido > 0:

                if y_inserido > 0:
                    print('As coordenadas inseridas levam ao primeiro quadrante.')

                elif y_inserido < 0:
                    print('As coordenadas inseridas levam ao quarto quadrante.')

                else:
                    print('As coordenadas inseridas se situam sobre o eixo x, à direita da origem.')

            elif x_inserido < 0:

                if y_inserido > 0:
                    print('As coordenadas inseridas levam ao segundo quadrante.')
                
                elif y_inserido < 0:
                    print('As coordenadas inseridas levam ao terceiro quadrante.')
                
                else:
                    print('As coordenadas inseridas se situam sobre o eixo x, à esquerda da origem.')

            else:
                if y_inserido > 0:
                    print('As coordenadas inseridas se situam sobre o eixo y, acima da origem.')
                                
                elif y_inserido < 0:
                    print('As coordenadas inseridas se situam sobre o eixo y, abaixo da origem')
                                
                else:
                    print('As coordenadas inseridas se situam sobre a origem.')

            continuar = input('Deseja tentar outro? y para sim, qualquer outra coisa para não.\n').strip().lower()
            #.strip tira espaços em branco, .lower faz com que o programa pegue Y como y
            
            if continuar == 'y':
                limpa_a_tela()
                continue
            
            else:
                limpa_a_tela()
                break
            
        except ValueError:
                    limpa_a_tela()
                    print ('Insira números para x e y, e nada mais.\n')
        
def escolher_rotina():
    while True:
        print('----MENU PRINCIPAL----')
        print('Opções disponíveis:')
        print('Par ou ímpar: 1')
        print('Classificação de idade: 2')
        print('Localizador de coordenadas do plano cartesiano: 3')
        print('Sair: 4')

        rotina = input('\nDigite o número atribuído ao programa, ou 4 para sair:\n')

        try:
            numero = int(rotina)
            match numero:
                case 1:
                    limpa_a_tela()
                    par_ou_impar()

                case 2:
                    limpa_a_tela()
                    grupo_etario()

                case 3:
                    limpa_a_tela()
                    plano_cartesiano()

                case 4:
                    limpa_a_tela()
                    print('Obrigado por usar o programa! Volte logo!')
                    break

                case _:
                    limpa_a_tela()
                    print('\nPor favor, insira um número válido!\n')
            
        except ValueError:
            limpa_a_tela()
            print('\nPor favor insira um número válido!\n')

def main():
     limpa_a_tela()
     nome_do_programa()
     autenticacao()
     escolher_rotina()

if __name__ == '__main__':
    main()

