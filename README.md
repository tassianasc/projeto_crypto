# 🎓 Projeto da Disciplina — Estrutura de Dados Avançados

**Professor:** Márcio Garrido  
**Aluna:** Tássia Nascimento
---

# 🔒 ASCII-Math Crypto

O objeitvo é demonstrar a aplicação da **Cifra Afim (Affine Cipher)** combinada com uma **Árvore Binária de Busca (BST)** para criptografar e descriptografar mensagens.  
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
python Crypto.py "Sua Mensagem"
```
**Saída:**

- Lista criptografada  
- Travessia pós-ordem da BST  
- Arquivo `Msg.json` gerado  

---

### 🔓 2. Descriptografar (Decrypt.py)

```bash
python Decrypt.py
```
**Saída:**

- Valor de `A⁻¹`
- Mensagem original restaurada

---

## 📝 Exemplo de `Msg.json`

```json
{
  "encrypted": [33, 201, 119, 87],
  "A": 5,
  "B": 8,
  "M": 256
}
```
## 🧪 Exemplo de Execução

```bash
python Crypto.py "Olá Mundo"
```
**Sequência Criptografada:**

[47, 228, 88, 255, 47, 88, 198, 88]

**Travessia Pós-Ordem da BST:**

[47, 88, 198, 255, 228, 88, 47]

**Arquivo Msg.json criado com sucesso!**

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License**.

