import sys
import json

#CONFIGURAÇÕES E CHAVE DE CRIPTOGRAFIA AFIM
M = 256  # Módulo (Tamanho do alfabeto ASCII estendido)
A = 5    # Multiplicador. Deve ser coprimo de M.
B = 8    # Deslocamento

def encrypt_char(char):
    """
    Criptografa um caractere usando a Cifra Afim: E(x) = ((A * x) + B) mod M.
    
    :param char: O caractere a ser criptografado.
    :return: O valor inteiro criptografado.
    """
    x = ord(char)
    y = ((A * x) + B) % M
    return y

#ESTRUTURA DE DADOS: ÁRVORE BINÁRIA DE BUSCA (BST)
class Node:
    """Representa um nó na BST."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Implementa as operações da BST e a travessia Pós-Ordem."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insere um novo valor criptografado na árvore."""
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def _post_order_traversal(self, node, result):
        """Função recursiva para travessia Pós-Ordem (Esquerda, Direita, Raiz)."""
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.value)

    def get_post_order(self):
        """Retorna a lista de valores na ordem Pós-Ordem para visualização gráfica."""
        result = []
        self._post_order_traversal(self.root, result)
        return result

#LÓGICA PRINCIPAL
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python Crypto.py \"<mensagem a ser criptografada>\"")
        sys.exit(1)

    original_message = sys.argv[1]
    bst = BST()
    ordered_encrypted_values = [] 
    
    print(f"\n[CRYPTO.PY] Mensagem Original: '{original_message}'")
    print(f"[CRYPTO.PY] Chave Afim (A, B, M): ({A}, {B}, {M})")

    for char in original_message:
        encrypted_val = encrypt_char(char)
        ordered_encrypted_values.append(encrypted_val) 
        bst.insert(encrypted_val) 

    post_order_list_for_display = bst.get_post_order() 
    
    print("\n VISUALIZAÇÃO BST: Ordem Pós-Ordem (GRÁFICO) ")
    print(post_order_list_for_display)
    
    print("\n DADO CRIPTOGRAFADO REAL (Sequência para JSON)")
    print(ordered_encrypted_values)
    
    json_output = {
        "encrypted_message_sequential": ordered_encrypted_values, 
        "bst_post_order_display": post_order_list_for_display, 
        "encryption_key": {"A": A, "B": B, "M": M}
    }

    try:
        with open('Msg.json', 'w') as f:
            json.dump(json_output, f, indent=4)
        print("\n Sucesso: Arquivo 'Msg.json' gerado com o conteúdo **sequencial**.")
    except Exception as e:
        print(f" Erro ao escrever o arquivo JSON: {e}")