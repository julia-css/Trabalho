"""
Violência Contra a Mulher – Teresina / PI  |  2020–2025
Landing page — app.py
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Violência Contra a Mulher – Teresina/PI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Reset global do Streamlit e Ajuste do Botão ───────────────────────────────
st.markdown("""
<style>
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebarNav"]     { display: none !important; }
[data-testid="stHeader"]         { display: none !important; }
.block-container                 { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewContainer"] { background: #0B0A0E !important; }

/* Nova regra para subir o bloco do botão */
.subir-botao {
    margin-top: -120px !important;  /* Puxa o botão para cima */
    position: relative;
    z-index: 99;                   /* Garante que ele fique clicável sobre o fundo */
}

div[data-testid="stButton"] button {
  background: #FF3D6B !important;
  color: #fff !important;
  border: none !important;
  padding: 16px 40px !important;
  font-size: 16px !important;
  font-weight: 500 !important;
  border-radius: 8px !important;
  font-family: 'DM Sans', sans-serif !important;
  transition: background .2s, transform .15s !important;
  cursor: pointer !important;
}
div[data-testid="stButton"] button:hover {
  background: #C91747 !important;
  transform: translateY(-2px) !important;
}
div[data-testid="stVerticalBlock"] {
  gap: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Hero via components.html (Ajustado o height para 580) ────────────────────
components.html("""
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0B0A0E; overflow: hidden; }

.lp-hero {
  min-height: 80vh; /* Ajustado ligeiramente para não empurrar a tela para baixo */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 60px 48px;
  position: relative;
  overflow: hidden;
  font-family: 'DM Sans', sans-serif;
  color: #F4EDF0;
  background: #0B0A0E;
}
.lp-hero::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 60% 60% at 80% 50%, rgba(255,61,107,0.12) 0%, transparent 70%),
    radial-gradient(ellipse 40% 50% at 20% 80%, rgba(201,23,71,0.08) 0%, transparent 60%);
  pointer-events: none;
}
.hero-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 40px;
  width: 100%;
  max-width: 1200px;
  position: relative;
  z-index: 1;
}
.hero-left { flex: 1; max-width: 680px; }
.hero-right {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
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
  animation: fadeUp .7s .25s ease both;
  color: #F4EDF0;
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
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  animation: fadeIn .9s .7s ease both;
}
.lp-ribbon-line { height: 3px; background: #FF3D6B; border-radius: 2px; }
.lp-ribbon-line:nth-child(1) { width: 180px; opacity: 0.8; margin-bottom: 12px; }
.lp-ribbon-line:nth-child(2) { width: 120px; opacity: 0.5; margin-bottom: 12px; }
.lp-ribbon-line:nth-child(3) { width:  60px; opacity: 0.3; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: none; }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@media (max-width: 768px) {
  .lp-hero      { padding: 60px 24px; }
  .hero-content { flex-direction: column; align-items: flex-start; }
  .lp-ribbon    { display: none; }
}
</style>
</head>
<body>
<div class="lp-hero">
  <div class="hero-content">
    <div class="hero-left">
      <p class="lp-eyebrow">Teresina &middot; Piau&iacute; &middot; 2020&ndash;2025</p>
      <h1 class="lp-title">
        Viol&ecirc;ncia contra<br>a <em>Mulher</em>
      </h1>
      <p class="lp-sub">
        Panorama da viol&ecirc;ncia contra a mulher na capital do Piau&iacute; (2020&ndash;2025).
      </p>
    </div>
    <div class="hero-right">
      <div class="lp-ribbon">
        <div class="lp-ribbon-line"></div>
        <div class="lp-ribbon-line"></div>
        <div class="lp-ribbon-line"></div>
      </div>
    </div>
</div>
</body>
</html>
""", height=500, scrolling=False)

container_botao = st.container()

with container_botao:
    st.markdown('<div class="subir-botao">', unsafe_allow_html=True)
    _, col_btn = st.columns([4, 2])
    with col_btn:
        if st.button("Acessar o Dashboard"):
            st.switch_page("pages/dashboard.py")
    st.markdown('</div>', unsafe_allow_html=True)
