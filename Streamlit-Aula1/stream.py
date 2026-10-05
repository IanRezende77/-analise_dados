import steamlit as st
import pandas as pd

# ==========================================
# 1 - Olá, mundo
# ==========================================

st.write("Olá, mundo")


# ==========================================
# 2 - Variáveis com nome e idade
# ==========================================

nome = "Ian"
idade = 16

st.write("Meu nome é", nome)
st.write("Minha idade é", idade)


st.divider()


# ==========================================
# 3 - Título e subtítulo
# ==========================================

st.title("Meu primeiro dash")
st.subheader(nome)


# ==========================================
# 4 - Criando o DataFrame
# ==========================================

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})


# Mostrando o DataFrame
st.write(df)


st.divider()


# ==========================================
# 5 - Caixa de seleção do supermercado
# ==========================================

st.subheader("Lista de supermercado")

produtos = {
    "Arroz": 25.00,
    "Feijão": 8.50,
    "Leite": 5.50,
    "Pão": 10.00,
    "Café": 15.00
}


produto = st.selectbox(
    "Escolha um produto:",
    list(produtos.keys())
)


# ==========================================
# 6 - Quantidade
# ==========================================

quantidade = st.number_input(
    "Escolha a quantidade:",
    min_value=1,
    value=1
)


# ==========================================
# 7 - Função para calcular o preço
# ==========================================

def calcular_preco(produto, quantidade):
    preco = produtos[produto]
    total = preco * quantidade
    return total


# Calculando o total
total = calcular_preco(produto, quantidade)


# ==========================================
# 8 - Mostrando o resultado
# ==========================================

st.metric(
    "Preço total da compra",
    f"R$ {total:.2f}"
)
