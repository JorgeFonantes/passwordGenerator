import re
# verificar comprimento e se tem os caracteres necessários:
def chk_passwrd(password):

    if len(password) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    
    if not re.search(r'[A-Z]', password):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    
    if not re.search(r'[a-z]', password):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    
    if not re.search(r'\d', password):
        return False, "A senha deve conter pelo menos um dígito."

  
    if not re.search(r'[@#$%^&+=]', password):
        return False, "A senha deve conter pelo menos um caractere especial (@, #, $, etc.)."

    return True, "A senha é forte."

# uso em prática, selecione primeiro uma senha no gerador de senhas para testar
password = input("Digite a senha para verificar: ")
is_strong, message = chk_passwrd(password)
if is_strong:
    print(message)
else:
    print(f"Senha fraca: {message}")
