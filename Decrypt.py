import json
import sys

#FERRAMENTA MATEMÁTICA: INVERSO MODULAR
def extended_gcd(a, b):
    """
    Implementa o Algoritmo Estendido de Euclides para encontrar o MDC e coeficientes.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a, m):
    """
    Calcula o Inverso Multiplicativo Modular de 'a' módulo 'm' (A^-1).
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception(f'Erro: Inverso modular de {a} mod {m} não existe.')
    else:
        return x % m

#LÓGICA DE DESCRIPTOGRAFIA
def decrypt_char(y, A_inv, B, M):
    """
    Descriptografa um valor (y) usando a Cifra Afim: D(y) = (A_inv * (y - B)) mod M.
    
    :param y: O valor inteiro criptografado.
    :param A_inv: O inverso multiplicativo modular de A.
    :return: O caractere decifrado.
    """
    subtracted = (y - B + M) % M
    x = (A_inv * subtracted) % M
    return chr(x)

#LÓGICA PRINCIPAL
if __name__ == '__main__':
    try:
        with open('Msg.json', 'r') as f:
            data = json.load(f)
            
        encrypted_list = data["encrypted_message_sequential"] 
        key = data["encryption_key"]
        
        A, B, M = key["A"], key["B"], key["M"]

    except FileNotFoundError:
        print(" Erro: Arquivo 'Msg.json' não encontrado. Execute Crypto.py primeiro.")
        sys.exit(1)
    except Exception as e:
        print(f" Erro ao ler ou processar 'Msg.json': {e}")
        sys.exit(1)
    
    print("\n[DECRYPT.PY] Iniciando Descriptografia...")

    try:
        A_inv = mod_inverse(A, M)
        print(f"  Chave de Descriptografia (A_inv): {A_inv}")
    except Exception as e:
        print(f" Erro na chave: {e}")
        sys.exit(1)
        
    decrypted_message = ""
    for val in encrypted_list:
        decrypted_message += decrypt_char(val, A_inv, B, M)
        
    print("\n==================================")
    print("▶ MENSAGEM REAL: ")
    print(f"**{decrypted_message}**")
    print("==================================")