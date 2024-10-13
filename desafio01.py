#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence 
# ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# Verifica se o numero pertence a sequência de Fibonacci
def isFibonacci(n):
    # Inicializando os dois primeiros números da sequência
    numeroPos1, numeroPos2 = 0, 1
    
    # Verificando se o número é 0 ou 1 caso for true retorna que faz parte da sequência
    if n == 0 or n == 1:
        return f"O número {n} faz parte da sequência de Fibonacci."
    
    # faz testes comparando a sequência de Fibonacci com o numero escolhido, caso for igual ou maior para a comparação
    while numeroPos2 < n:
        numeroPos1, numeroPos2 = numeroPos2, numeroPos1 + numeroPos2
    
    # Verificando se o número faz parte da sequência
    if numeroPos2 == n:
        return f"O número {n} faz parte da sequência de Fibonacci."
    else:
        return f"O número {n} não faz parte da sequência de Fibonacci."

def main():
    # Solicita ao usuario um numero
    numero = int(input("Informe um número: "))
    # coloca na variavel resultado o que a função isFibonacci retornou
    resultado = isFibonacci(numero)
    # printa na tela se o numero faz ou não parte da sequência de Fibonacci
    print(resultado)

# Garante que a função main seja executada apenas quando o codigo for aberto diretamente, e não quando for importado para outro codigo
if __name__ == "__main__":
    main()