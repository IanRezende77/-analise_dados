import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Supermercado do Ian",
    page_icon="🛒",
    layout="centered"
)

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


# ==========================================
# 9 - Calculadora de troco
# ==========================================

st.divider()
st.subheader("Calculadora de Troco")

col1, col2 = st.columns(2)

with col1:
    valor_compra = st.number_input(
        "Valor da compra:",
        value=float(total),
        step=1.0
    )

with col2:
    dinheiro_pago = st.number_input(
        "Dinheiro pago:",
        value=0.0,
        step=1.0
    )


# Botão para calcular o troco
if st.button("Calcular Troco", type="primary"):
    if dinheiro_pago < valor_compra:
        st.error("O valor pago é menor que o valor da compra.")
    else:
        resultado = dinheiro_pago - valor_compra
        st.success(f"**Troco:** R$ {resultado:.2f}")
