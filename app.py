import subprocess
import streamlit as st
from PIL import Image
import os
import csv
import glob
import datetime

import base64
# Executa o ControlePinhal.py apenas uma vez na abertura do app
if 'controlepinhal_rodado' not in st.session_state:
    subprocess.run(["python", "ControlePinhal.py"], check=True)
    st.session_state['controlepinhal_rodado'] = True

st.set_page_config(layout="wide", page_title="Projeto Pinhal")

# Lê o resumo
resumo_dict = {}
with open('resumo.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        resumo_dict[row['Categoria']] = row
        #print(row)
        
descricoes = ['Entradas','Receitas','Aporte','Despesas','OPEX','CAPEX','Impostos']
        
# Sidebar com logo e menu
with st.sidebar:
    st.image("logotipo.png", use_container_width=True)
    st.title("Painel Financeiro")
    st.markdown("Projeto de Iluminação Espírito Santo de Pinhal - SP")
    st.markdown("---")
    hoje = datetime.datetime.now()
    mes_anterior = hoje.replace(day=1) - datetime.timedelta(days=1)
    mes_anterior_str = mes_anterior.strftime('%m')
    st.markdown(f'<div style="font-size:1em; color:#123366; margin-bottom:0.5em;">Período: mês 10-24 até mês {mes_anterior_str}-25 </div>', unsafe_allow_html=True)
    page = st.radio("Menu", ["Resumo", "Gráficos", "Balancetes"])

# Autenticação simples por senha
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.markdown('<h2 style="color:#123366;">Acesso Restrito</h2>', unsafe_allow_html=True)
    senha = st.text_input('Digite a senha para acessar o painel:', type='password')
    if st.button('Entrar'):
        if senha == 'Pinhal2025':  # Troque por uma senha forte
            st.session_state['autenticado'] = True
            st.success('Acesso liberado!')
            #st.experimental_rerun()
        else:
            st.error('Senha incorreta!')
    st.stop()
st.markdown('<h1 style="font-size: 4em; color:#123366; margin-bottom:0.2em; text-align:center;">Projeto Pinhal</h1>', unsafe_allow_html=True)

if page == "Resumo":
    st.markdown('<h1 style="font-size:2em; color:#123366; margin-bottom:0.2em; text-align:center;">Resumo Financeiro</h1>', unsafe_allow_html=True)
    descricoes = ['Entradas','Receitas','Aporte','Despesas','OPEX','CAPEX','Impostos']
    for nome in descricoes:
        st.markdown(f'<h1 style="text-align:left; color:#123366; font-size:1.3em; margin-bottom:0.2em;">{nome}</h1>', unsafe_allow_html=True)
        r = resumo_dict[nome]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(f"{nome} Orçado no Período", f"R$ {float(r['Total Orçado']):,.0f}".replace(",", "."))
        with col2:
            st.metric(f"{nome} Realizado no Período", f"R$ {float(r['Total Realizado']):,.0f}".replace(",", "."))
        with col3:
            st.metric(f"Execução {nome} (%)", f"{float(r['Razao'])*100:.1f}%")
        st.markdown('<hr style="height:2px;border:none;background:linear-gradient(90deg,rgba(18,51,102,0.18) 0%,rgba(46,196,182,0.18) 100%);border-radius:1px;margin:1px 0 1px 0;">', unsafe_allow_html=True)

elif page == "Gráficos":
    st.markdown('<h1 style="font-size:2em; color:#123366; margin-bottom:0.2em; text-align:center;">Gráficos Financeiro</h1>', unsafe_allow_html=True)
    descricoes = ['Entradas','Receitas','Aporte','Despesas','OPEX','CAPEX','Impostos']
    for nome in descricoes:
        img_path = f"Imagens/{nome}.png"
        linha_path = f"Imagens/{nome}_linha.png"
        st.markdown(f'<h1 style="text-align:left; color:#123366; font-size:1.3em; margin-bottom:0.2em;">{nome}</h1>', unsafe_allow_html=True)
        col_barra, col_linha = st.columns(2)
        with col_barra:
            st.markdown('<div style="text-align:center; font-weight:bold; color:#123366;">Barras</div>', unsafe_allow_html=True)
            if os.path.exists(img_path):
                img = Image.open(img_path)
                width = int(img.width * 0.8)
                st.image(img, width=width, caption=nome)
            else:
                st.warning(f"Gráfico {nome}.png não encontrado.")
        with col_linha:
            st.markdown('<div style="text-align:center; font-weight:bold; color:#2ec4b6;">Linha</div>', unsafe_allow_html=True)
            if os.path.exists(linha_path):
                img_linha = Image.open(linha_path)
                width_linha = int(img_linha.width * 0.8)
                st.image(img_linha, width=width_linha, caption=nome+" (linha)")
            else:
                st.warning(f"Gráfico {nome}_linha.png não encontrado.")
        st.markdown('<hr style="height:2px;border:none;background:linear-gradient(90deg,rgba(18,51,102,0.18) 0%,rgba(46,196,182,0.18) 100%);border-radius:1px;margin:1px 0 1px 0;">', unsafe_allow_html=True)

elif page == "Balancetes":
    st.markdown('<h1 style="font-size:2em; color:#123366; margin-bottom:0.2em; text-align:center;">Balancetes - Upload, Visualização e Download</h1>', unsafe_allow_html=True)

    uploaded_pdf = st.file_uploader("Faça upload de um PDF de balancete", type=["pdf"])
    if uploaded_pdf is not None:
        st.success(f"Arquivo '{uploaded_pdf.name}' enviado com sucesso!")
        st.download_button(f"Baixar {uploaded_pdf.name}", uploaded_pdf, file_name=uploaded_pdf.name)
    st.markdown('<h3 style="font-size:1em; color:#123366; margin-bottom:0.2em;">Arquivos disponíveis:</h3>', unsafe_allow_html=True)
    import glob
    pdfs = glob.glob("Balancetes/*.pdf")
    for pdf in pdfs:
        nome_pdf = os.path.basename(pdf)
        with open(pdf, "rb") as f:
            st.download_button(f"Baixar {nome_pdf}", f, file_name=nome_pdf)

