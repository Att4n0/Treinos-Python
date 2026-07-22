print('\n𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔\n')

print ('1. Cadastrar restaurante')
print ('2. Listar restaurantes')
print ('3. Ativar restaurante')
print ('4. Sair\n')

#opcao_escolhida = input ('Escolha uma opção: ') Não funciona aqui, porque a entrada, por padrão, é uma string. 
# Duas opções:

#Após o input que dá em string, faz uma ova variável que transforma o string em int:
#opcao_escolhida = int(opcao_escolhida)
#É, pode usar o mesmo nome de variável, mesmo.

#OU:

opcao_escolhida = int(input ('Escolha uma opção: '))

if opcao_escolhida == 1:
    print ('Cadastrar Restaurante')


elif opcao_escolhida == 2:
    print ('Listar Restaurantes')


elif opcao_escolhida == 3:
    print ('Ativar Restaurante')


elif opcao_escolhida == 4:
    print ('Encerrando o programa')

else:
    print ('São quatro opções, bundão. Escolhe uma e digite o número de 1 a 4. Não é difícil.')