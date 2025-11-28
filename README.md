# 🔒 ASCII-Math Crypto

Este projeto demonstra a aplicação da **Cifra Afim (Affine Cipher)** combinada com uma **Árvore Binária de Busca (BST)** para criptografar e descriptografar mensagens.  
O sistema transforma um texto em valores numéricos criptografados, armazena a saída em JSON e reconstrói a mensagem original aplicando o inverso modular.

---

## 📁 Estrutura do Projeto

```plaintext
📦 PROJETOCRYPTO
 ┣ 📜 Crypto.py
 ┣ 📜 Decrypt.py
 ┣ 📜 Msg.json
 ┗ 📜 README.md
```
## 🔑 Criptografia Utilizada — Affine Cipher

A Cifra Afim é definida pela fórmula:

`E(x) = (A * x + B) mod M`

### 🔢 Parâmetros utilizados

| Parâmetro | Valor | Descrição               |
|----------|-------|-------------------------|
| `M`      | 256   | ASCII estendido         |
| `A`      | 5     | Multiplicador           |
| `B`      | 8     | Deslocamento            |
| `A⁻¹`    | —     | Calculado no programa – inverso multiplicativo |

### 🔄 Fórmula de Descriptografia

`D(y) = (A⁻¹ * (y - B)) mod M`

---

## 🌳 Estrutura de Dados — BST

Durante a criptografia:

- Cada valor criptografado é inserido em uma **Binary Search Tree**.
- O console exibe uma **travessia Pós-Ordem** para visualização.

> 💡 A BST é apenas representacional.  
> A ordem real da mensagem é preservada no arquivo `Msg.json`.

---

## 🚀 Como Executar

Requer **Python 3.10+**.

### 🔐 1. Criptografar (Crypto.py)

```bash
python Crypto.py "Sua Mensagem Secreta Aqui"
