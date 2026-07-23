import os
#Pra detectar o sistema operacional lá em baixo

import subprocess
#Pra dar instruções para programas externos. O clear, do bash, é um executável externo.
#O subprocess, em teoria, é mais seguro e moderno do que o import os. Vale dar uma conferida.
#Onde puder usar o subprocess no lugar do os, talvez seja melhor. Mas pesquisa, antes.

def exibir_nome_do_programa():
    print('\n𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔\n')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurantes')
    print ('3. Ativar restaurante')
    print ('4. Sair\n')

def escolher_opcao():
    #opcao_escolhida = input ('Escolha uma opção: ') Não funciona aqui, porque a entrada, por padrão, é uma string. 
    # Duas opções:

    #Após o input que dá em string, faz uma ova variável que transforma o string em int:
    #opcao_escolhida = int(opcao_escolhida)
    #É, pode usar o mesmo nome de variável, mesmo.

    #OU:

    opcao_escolhida = int(input ('Escolha uma opção: '))
    #poderia usar if elif e else, ou:
    match opcao_escolhida:
        case 1:
            print ('Cadastrar Restaurante')


        case 2:
            print ('Listar Restaurantes')


        case 3:
            print ('Ativar Restaurante')

        case 4:
            finalizar_app()

        case _:
            print ('São quatro opções, bundão. Escolhe uma e digite o número de 1 a 4. Não é difícil.')

def finalizar_app():
    if os.name == 'nt':
        #nt, aqui, delimita o windows.
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])
        #Pra linux e Mac

        #Podia ter usado o "os.system('clear')", mas, se puder, evita o os.
    
    print('Finalizando...\n')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()