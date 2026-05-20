"""
Violência Contra a Mulher – Teresina / PI  |  2020–2025
Landing page — app.py  (primeira tela ao abrir o Streamlit)
"""

import streamlit as st

st.set_page_config(
    page_title="Violência Contra a Mulher – Teresina/PI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');
[data-testid="collapsedControl"] { display: none !important; }
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --pink:    #FF3D6B;
  --pink-dk: #C91747;
  --bg:      #0B0A0E;
  --text:    #F4EDF0;
  --muted:   #9A8A93;
  --border:  rgba(255,61,107,0.18);
}

/* Reset Streamlit */
[data-testid="stAppViewContainer"] {
  background: #0B0A0E !important;
}
[data-testid="stHeader"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

/* Hero */
.lp-hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 80px 80px;
  position: relative;
  overflow: hidden;
  font-family: 'DM Sans', sans-serif;
  color: #F4EDF0;
}
.lp-hero::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 60% 60% at 80% 50%, rgba(255,61,107,0.12) 0%, transparent 70%),
    radial-gradient(ellipse 40% 50% at 20% 80%, rgba(201,23,71,0.08) 0%, transparent 60%);
  pointer-events: none;
}
.lp-eyebrow {
  font-size: 12px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #FF3D6B;
  font-weight: 500;
  margin-bottom: 24px;
  animation: fadeUp .7s .1s ease both;
}
.lp-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(48px, 7vw, 88px);
  font-weight: 900;
  line-height: 1.04;
  letter-spacing: -1px;
  max-width: 820px;
  animation: fadeUp .7s .25s ease both;
}
.lp-title em {
  font-style: normal;
  color: #FF3D6B;
}
.lp-sub {
  margin-top: 28px;
  font-size: 18px;
  color: #9A8A93;
  max-width: 520px;
  font-weight: 300;
  line-height: 1.7;
  animation: fadeUp .7s .4s ease both;
}
.lp-ribbon {
  position: absolute; right: 0; top: 50%;
  transform: translateY(-50%);
  display: flex; flex-direction: column; align-items: flex-end; gap: 0;
  animation: fadeIn .9s .7s ease both;
}
.lp-ribbon-line { height: 3px; background: #FF3D6B; border-radius: 2px 0 0 2px; }
.lp-ribbon-line:nth-child(1) { width: 180px; opacity: 0.8; margin-bottom: 12px; }
.lp-ribbon-line:nth-child(2) { width: 120px; opacity: 0.5; margin-bottom: 12px; }
.lp-ribbon-line:nth-child(3) { width: 60px;  opacity: 0.3; }

.lp-footer {
  text-align: center;
  padding: 28px 48px;
  background: #12101A;
  border-top: 1px solid rgba(255,61,107,0.18);
  font-family: 'DM Sans', sans-serif;
  font-size: 12px;
  color: #9A8A93;
  line-height: 1.8;
}
.lp-footer strong {
  font-family: 'Playfair Display', serif;
  font-size: 15px;
  color: #F4EDF0;
  display: block;
  margin-bottom: 4px;
}
.lp-footer span { color: #FF3D6B; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: none; }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* Botão Streamlit customizado */
div[data-testid="stButton"] button {
  background: #FF3D6B !important;
  color: #fff !important;
  border: none !important;
  padding: 16px 40px !important;
  font-size: 16px !important;
  font-weight: 500 !important;
  border-radius: 8px !important;
  font-family: 'DM Sans', sans-serif !important;
  margin-top: 44px !important;
  transition: background .2s, transform .15s !important;
  cursor: pointer !important;
}
div[data-testid="stButton"] button:hover {
  background: #C91747 !important;
  transform: translateY(-2px) !important;
}
</style>

<div class="lp-hero">
  <p class="lp-eyebrow">Teresina · Piauí · 2020–2025</p>
  <h1 class="lp-title">Violência contra<br>a <em>Mulher</em></h1>
  <p class="lp-sub">
    Dados oficiais sobre violência de gênero registrados em Teresina entre 2020 e 2025.
    Explore o painel interativo para filtrar, comparar e visualizar as informações.
  </p>
  <div class="lp-ribbon">
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  /* Container fixo e centralizado na lateral direita */
  .container-direita {
    position: fixed;
    right: 40px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 999;
  }

  /* Estilização da imagem com a identidade visual do site */
  .imagem-piaui {
    width: 280px;
    height: auto;
    border-radius: 16px;
    border: 3px solid #FF3D6B; /* Borda com a cor predominante */
    /* Sombra suave combinando com o tom #FF3D6B */
    box-shadow: 0px 8px 24px rgba(255, 61, 107, 0.2); 
    transition: transform 0.3s ease; /* Efeito suave ao passar o mouse */
  }

  /* Efeito interativo quando o usuário passa o mouse */
  .imagem-piaui:hover {
    transform: scale(1.03);
  }
</style>

<div class="container-direita">
  <img src="piaui.png" class="imagem-piaui" alt="Imagem do Piauí">
</div>
""", unsafe_allow_html=True)



col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Acessar o Dashboard"):
        st.switch_page("pages/dashboard.py")

st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Violência Contra a Mulher – Teresina/PI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

