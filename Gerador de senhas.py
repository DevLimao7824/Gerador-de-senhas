import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def app_senha():
    tamanho = int(input("Qual o tamanho da senha? "))
    senha = gerar_senha(tamanho)
    print(f"Sua senha gerada: {senha}")

app_senha()