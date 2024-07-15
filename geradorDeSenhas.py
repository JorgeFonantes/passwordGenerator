import string as st
import numpy as np
#função para criar a senha

def generate_strong_password(length=12):
    letter = st.ascii_letters
    number = st.digits
    special = st.punctuation
    total = letter + number + special
    
    while True:
        pw = np.random.choice(list(total), length)
        password = ''.join(pw)
        
        #algaritmo para verificar se a senha é forte o suficiente
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in special for char in password)
        
        if has_upper and has_lower and has_digit and has_special:
            return password

#criar a senha :)
strngPassw = generate_strong_password(12)
print(strngPassw)
