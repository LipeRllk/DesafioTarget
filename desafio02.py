#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# Biblioteca importada para retira os acentos da string
from unidecode import unidecode

# Função para verificar a existência da letra 'a' (maiúscula ou minúscula) e contar suas ocorrências
def verifiString(textoAcento):
    # Utilizando a biblioteca unicode, retira os acentos da string
    texto = unidecode(textoAcento)
    # Converte toda a string para caixa baixa e conta a existencia das letras a na string
    contagem = texto.lower().count('a')
    
    # Verifica a existencia de letras "a" na string
    if contagem > 0:
        # Caso tenha mais de 1 letra "a" retorna
        return f"A letra 'a' ocorre {contagem} vezes na string."
    else:
        # Caso n'ao exista letras "a" na string 
        return "A letra 'a' não foi encontrada na string."

# Exemplo de uso com uma string definida

def main():
    string = str(input("digite a string que deseja verificar a existencia da letra 'a': "))
    resultado = verifiString(string)
    print(resultado)

# Garante que a função main seja executada apenas quando o codigo for aberto diretamente, e não quando for importado para outro codigo
if __name__ == "__main__":
    main()