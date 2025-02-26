# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

string_repetida = (string + " ") * numero

print(string_repetida)