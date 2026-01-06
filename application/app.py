# Impotar a biblioteca Streamlit e dá o apelido "st"
# Streanlit é usado para criar aplicações web interativas de forma simples com Python
import streamlit as st

# Importar a biblioteca os
#Ela permite trabalhar com caminhos e arquivos do sistemas
import os

# ------------------------
# Configuração da página
# ------------------------

# Define o título que aparece na aba do navegador
st.set_page_config(page_title="Gestão de Estoque de Veículos", layout="centered")

#Título principal da página
st.title("Gestão de Estoque de Veículos")

#Texto menor abaixo do título
st.subheader("Projeto em construção")

#Linha divisória visual
st.divider()

# ------------------------
# CAMINHO DO ARQUIVO CSV
# ------------------------

#Cria o caminho do arquivo onde os dados serão salvos
CAMINHO_ARQUIVO = "../data/estoque_veiculos.csv"

#Se o arquivo ainda não existir, cria ele com o cabeçalho
if not os.path.exists(CAMINHO_ARQUIVO):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo: arquivo.write("modelo,quantidade,estoque_min,estoque_max\n")

# ------------------------
# FORMULÁRIO DE CADASTRO
# ------------------------

st.subheader("Cadastro de Veículo")

#Campo para digitar o modelo do veículo
modelo = st.text_input("Modelo do veículo")

# Campo numérico para a quantidade atual em estoque
quantidade = st.number_input("Quantidade em estoque", min_value=0, step=1)

# Campo numérico para o estoque mínimo
estoque_min = st.number_input("Estoque mínimo", min_value=0, step=1)

# Campo numérico para o estoque máximo
estoque_max = st.number_input("Estoque máximo", min_value=0, step=1)

# Botão para cadastrar
cadastrar = st.button("Cadastrar Veículo")

# ------------------------
# AÇÃO DO BOTÃO
# ------------------------

if cadastrar:
    # Validação simples
    if modelo == "":
        st.error("O modelo do veículo não pode ficar vazio.")
    else:
        # Abre o arquivo em modo 'append' (adicionar no final)
        with open (CAMINHO_ARQUIVO, "a", encoding="utf-8") as arquivo: arquivo.write(f"{modelo},{quantidade},{estoque_min},{estoque_max}\n")

        # Mensagem de sucesso
        st.success("Veículo cadastrado com sucesso!")
