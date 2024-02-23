# Importações

import re
from time import sleep

# Variáveis testes

# senhas = [
        # "P@ssw0rd!",
        # "Segura#2024",
        # "SenhaV@lid4!",
        # "12@34",
        # "!Senha12@34",
        # "12345678",
        # "Abcdefg",
        # "123Aa!45",
        # "p@ssw0rd",
        # "Senha"]

# Função para validar se a senha atende aos requisitos

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])()(?=.*[!@#$%]).{8,}$'    
        
    if re.match(padrao, senha):
        return True
    else:
        return False

# Programa Principal

def main():
    print('-' * 45)
    print("\033[1;44mBem vindo ao programa de validação de senhas!\033[m")
    print('-' * 45)

    print("""Crie uma senha que atenda os seguintes requisitos:
1. Deve ter pelo menos 8 caracteres.
2. Deve conter pelo menos uma letra maiúscula e uma letra minúscula.
3. Deve conter pelo menos um caractere especial (considere apenas esses: ! @ # $ %).""")
    while True: #Terror do Santi
        senha = input("\033[36mDigite uma senha: \033[m ")
        if validar_senha(senha):
            print(f"A sua senha é ótima! Utilize-a: {senha}")
            sleep(2)
            break
        else:
            print(f'Tente novamente.')         


main()
