"""
Violência Contra a Mulher – Teresina / PI  |  2020–2025
Página: Sobre o Projeto — pages/sobre.py

IMPORTANTE: Este arquivo DEVE estar na pasta  pages/  (subpasta do app.py).
O Streamlit detecta automaticamente todos os arquivos em pages/ e os exibe
como páginas no menu lateral.
"""

import streamlit as st
from pathlib import Path

# ── Configuração da página ────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sobre o Projeto · VCM Teresina",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS  (reutiliza o mesmo style.css do app principal) ───────────────────────
def inject_css_sobre() -> None:
    css_path = Path(__file__).parent.parent / "style.css"
    if css_path.exists():
        css_raw = css_path.read_text(encoding="utf-8")
        # tema padrão Rosa para a página Sobre
        st.markdown(f"""
        <style>
        :root {{
            --primary:    #FF4081;
            --secondary:  #F50057;
            --accent:     #1A1A1A;
            --bg:         #000000;
            --card_bg:    #111111;
            --text:       #FFFFFF;
            --subtext:    #AAAAAA;
            --sidebar_bg: #0D0D0D;
        }}
        {css_raw}
        </style>
        """, unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

inject_css_sobre()

# ── Link de volta ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Sobre o Projeto")
    st.divider()
    st.page_link("app.py", label="Voltar ao Dashboard")

# ── Cabeçalho ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1>Sobre o Projeto</h1>
  <p>Violência Contra a Mulher – Teresina / PI · 2020–2025</p>
</div>
""", unsafe_allow_html=True)

# ── Fontes ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Nota Metodológica</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="alert-box">
<b>Sobre os dados:</b> Os registros apresentados foram construídos com base nas proporções
e volumes reais publicados pelas seguintes fontes oficiais:<br><br>

• <b>SSP/PI</b> – Secretaria de Segurança Pública do Piauí
  (volumes anuais por zona/delegacia)<br>

• <b>SINAN/MS</b> – Sistema de Informação de Agravos de Notificação do Ministério da Saúde
  (distribuição por faixa etária e tipo de violência)<br>

• <b>Observatório Mulher Teresina – SMPM</b> – 1º Boletim OMT 2022
  (perfil das vítimas)<br>

• <b>Rede Observatórios da Segurança</b> – Relatório <i>Elas Vivem</i> 2025
  (volumes: Teresina concentra 42,6% dos casos do Piauí; 2024: 101 ocorrências graves;
  agressor prevalente: cônjuge/ex-cônjuge)<br>

• <b>Delegacias Especializadas de Atendimento à Mulher (DEAM)</b>
  (coberturas por zona da cidade)<br><br>

<b>Observação:</b> 2025 representa dados parciais do 1º semestre.
Os números individualizados foram gerados para representação estatística proporcional
e <b>não substituem</b> os microdados oficiais da SSP/PI.
</div>
""", unsafe_allow_html=True)
