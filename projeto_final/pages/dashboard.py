"""
Violência Contra a Mulher – Teresina / PI  |  2020–2025
Dashboard principal — pages/dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════
# 1.  CONFIGURAÇÃO DA PÁGINA
# ═══════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Dashboard · VCM Teresina",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════════
# 2.  TEMAS DE CORES
# ═══════════════════════════════════════════════════════════════════
TEMAS: dict = {
    "Preto": {
        "primary":      "#FF4081",
        "secondary":    "#F50057",
        "accent":       "#1A1A1A",
        "bg":           "#000000",
        "card_bg":      "#111111",
        "text":         "#FFFFFF",
        "subtext":      "#AAAAAA",
        "sidebar_bg":   "#0D0D0D",
        "chart_colors": ["#FF4081","#F50057","#FF80AB","#FF6090","#C51162","#FF1744","#FF6D00"],
    },
    "Azul Escuro": {
        "primary":      "#0D47A1",
        "secondary":    "#1565C0",
        "accent":       "#E3F2FD",
        "bg":           "#0A1929",
        "card_bg":      "#0D2137",
        "text":         "#E3F2FD",
        "subtext":      "#90CAF9",
        "sidebar_bg":   "#0D2137",
        "chart_colors": ["#1565C0","#1976D2","#2196F3","#42A5F5","#0D47A1","#1E88E5","#64B5F6"],
    },
    "Roxo": {
        "primary":      "#B78AD4",
        "secondary":    "#8E24AA",
        "accent":       "#F3E5F5",
        "bg":           "#1A0D2B",
        "card_bg":      "#2E0A3B",
        "text":         "#F3E5F5",
        "subtext":      "#CE93D8",
        "sidebar_bg":   "#2E0A3B",
        "chart_colors": ["#8E24AA","#6A1B9A","#AB47BC","#BA68C8","#4A148C","#7B1FA2","#E1BEE7"],
    },
}

# ═══════════════════════════════════════════════════════════════════
# 3.  CSS
# ═══════════════════════════════════════════════════════════════════
def inject_css(t: dict) -> None:
    css_path = Path(__file__).parent.parent / "style.css"
    css_raw  = css_path.read_text(encoding="utf-8")
    st.markdown(f"""
    <style>
    :root {{
        --primary:    {t['primary']};
        --secondary:  {t['secondary']};
        --accent:     {t['accent']};
        --bg:         {t['bg']};
        --card_bg:    {t['card_bg']};
        --text:       {t['text']};
        --subtext:    {t['subtext']};
        --sidebar_bg: {t['sidebar_bg']};
    }}
    {css_raw}
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# 4.  DADOS
# ═══════════════════════════════════════════════════════════════════
@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_excel(
        Path(__file__).parent.parent / "violencia_mulher_teresina.xlsx",
        sheet_name="Dados Brutos",
        header=2,
    )

df_raw = load_data()

# ═══════════════════════════════════════════════════════════════════
# 5.  SIDEBAR
# ═══════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### Violência contra a Mulher")
    st.markdown("**Teresina – Piauí | 2020–2025**")
    st.divider()

    tema_escolhido = st.selectbox("Tema de cores", list(TEMAS.keys()), index=0)
    t = TEMAS[tema_escolhido]
    inject_css(t)

    st.divider()
    st.markdown("### Filtros")

    anos_sel = st.multiselect(
        "Ano",
        sorted(df_raw["Ano"].unique()),
        default=sorted(df_raw["Ano"].unique()),
    )
    st.divider()

    zonas_sel = st.multiselect(
        "Zona",
        sorted(df_raw["Zona"].unique()),
        default=sorted(df_raw["Zona"].unique()),
    )
    st.divider()

    tipos_sel = st.multiselect(
        "Tipo de Violência",
        sorted(df_raw["Tipo de Violência"].unique()),
        default=sorted(df_raw["Tipo de Violência"].unique()),
    )
    st.divider()

    faixas_sel = st.multiselect(
        "Faixa Etária",
        sorted(df_raw["Faixa Etária"].unique(), key=lambda x: int(x.split()[0])),
        default=sorted(df_raw["Faixa Etária"].unique(), key=lambda x: int(x.split()[0])),
    )
    st.divider()

    st.page_link("pages/sobre.py", label="Sobre o Projeto")

# ═══════════════════════════════════════════════════════════════════
# 6.  FILTRO DOS DADOS
# ═══════════════════════════════════════════════════════════════════
df = df_raw[
    df_raw["Ano"].isin(anos_sel) &
    df_raw["Zona"].isin(zonas_sel) &
    df_raw["Tipo de Violência"].isin(tipos_sel) &
    df_raw["Faixa Etária"].isin(faixas_sel)
].copy()

if df.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════
# 7.  CABEÇALHO
# ═══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="page-header">
  <h1>Violência Contra a Mulher – Teresina / PI</h1>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# 8.  KPIs
# ═══════════════════════════════════════════════════════════════════
total         = int(df["Nº de Casos"].sum())
anos_count    = df.groupby("Ano")["Nº de Casos"].sum()
media_anual   = int(anos_count.mean()) if len(anos_count) > 0 else 0
tipo_mais     = df.groupby("Tipo de Violência")["Nº de Casos"].sum().idxmax()
zona_mais     = df.groupby("Zona")["Nº de Casos"].sum().idxmax()
agressor_mais = df.groupby("Perfil do Agressor")["Nº de Casos"].sum().idxmax()

def metric_card(col, label: str, value: str, delta: str = "") -> None:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta">{delta}</div>
        </div>""", unsafe_allow_html=True)

k1, k2, k3, k4, k5 = st.columns(5)
metric_card(k1, "Total de Casos", f"{total:,}".replace(",", "."),"período filtrado")
metric_card(k2, "Média Anual", f"{media_anual:,}".replace(",", "."), "casos/ano")
metric_card(k3, "Tipo Mais Frequente",   tipo_mais[:22])
metric_card(k4, "Zona com Mais Casos",   zona_mais)
metric_card(k5, "Agressor Prevalente",   agressor_mais[:22])

# ═══════════════════════════════════════════════════════════════════
# 9.  HELPER DE LAYOUT DOS GRÁFICOS
# ═══════════════════════════════════════════════════════════════════
PCOLOR     = t["chart_colors"]
PLOT_BG    = t["card_bg"]
FONT_COLOR = t["text"]

def fig_layout(fig, title: str = ""):
    fig.update_layout(
        title=dict(text=title, font=dict(size=14, color=FONT_COLOR), x=0.01),
        paper_bgcolor=PLOT_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(color=FONT_COLOR, size=11),
        margin=dict(l=10, r=10, t=44, b=10),
        legend=dict(bgcolor=PLOT_BG, font=dict(color=FONT_COLOR, size=10)),
    )
    fig.update_xaxes(
        gridcolor="rgba(128,128,128,0.15)",
        linecolor="rgba(128,128,128,0.15)",
        color=FONT_COLOR,
    )
    fig.update_yaxes(
        gridcolor="rgba(128,128,128,0.15)",
        linecolor="rgba(128,128,128,0.15)",
        color=FONT_COLOR,
    )
    return fig

# ═══════════════════════════════════════════════════════════════════
# 10. SEÇÃO 1 – EVOLUÇÃO TEMPORAL
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Evolução Temporal</div>', unsafe_allow_html=True)

col_ev, col_anual = st.columns([3, 2])

with col_ev:
    ev = df.groupby(["Ano", "Tipo de Violência"])["Nº de Casos"].sum().reset_index()
    fig = px.line(
        ev, x="Ano", y="Nº de Casos", color="Tipo de Violência",
        markers=True, color_discrete_sequence=PCOLOR,
        labels={"Nº de Casos": "Casos", "Tipo de Violência": "Tipo"},
    )
    fig.update_traces(line=dict(width=2.5), marker=dict(size=7))
    fig_layout(fig, "Casos por Tipo de Violência ao Longo dos Anos")
    st.plotly_chart(fig, use_container_width=True)

with col_anual:
    anual = df.groupby("Ano")["Nº de Casos"].sum().reset_index()
    fig2 = px.bar(
        anual, x="Ano", y="Nº de Casos",
        color="Nº de Casos", color_continuous_scale=[PCOLOR[-1], PCOLOR[0]],
        text="Nº de Casos",
    )
    fig2.update_traces(textposition="outside", textfont_size=10)
    fig_layout(fig2, "Total Anual de Casos")
    fig2.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════
# 11. SEÇÃO 2 – DISTRIBUIÇÃO GEOGRÁFICA
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Distribuição Geográfica</div>', unsafe_allow_html=True)

col_zona, col_zona_ev = st.columns([1, 2])

with col_zona:
    zona_tot = (
        df.groupby("Zona")["Nº de Casos"].sum()
          .reset_index()
          .sort_values("Nº de Casos")
    )
    fig3 = px.bar(
        zona_tot, x="Nº de Casos", y="Zona", orientation="h",
        color="Zona", color_discrete_sequence=PCOLOR,
        text="Nº de Casos",
    )
    fig3.update_traces(textposition="outside")
    fig_layout(fig3, "Registros por Zona")
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

with col_zona_ev:
    ev_zona = df.groupby(["Ano", "Zona"])["Nº de Casos"].sum().reset_index()
    fig4 = px.line(
        ev_zona, x="Ano", y="Nº de Casos", color="Zona",
        markers=True, color_discrete_sequence=PCOLOR,
        labels={"Nº de Casos": "Casos"},
    )
    fig4.update_traces(line=dict(width=2.5), marker=dict(size=7))
    fig_layout(fig4, "Evolução Anual por Zona")
    st.plotly_chart(fig4, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════
# 12. SEÇÃO 3 – TIPOS, FAIXA ETÁRIA E PERFIL DO AGRESSOR
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Tipos de Violência & Perfis</div>', unsafe_allow_html=True)

col_tipo, col_faixa, col_agr = st.columns(3)

with col_tipo:
    tipo_tot = df.groupby("Tipo de Violência")["Nº de Casos"].sum().reset_index()
    fig5 = px.pie(
        tipo_tot, names="Tipo de Violência", values="Nº de Casos",
        color_discrete_sequence=PCOLOR, hole=0.42,
    )
    fig5.update_traces(textposition="inside", textinfo="percent+label", textfont_size=10)
    fig_layout(fig5, "Distribuição por Tipo")
    fig5.update_layout(showlegend=False)
    st.plotly_chart(fig5, use_container_width=True)

with col_faixa:
    faixa_tot = (
        df.groupby("Faixa Etária")["Nº de Casos"].sum()
          .reset_index()
          .sort_values("Faixa Etária", key=lambda x: x.map(lambda v: int(v.split()[0])))
    )
    fig6 = px.bar(
        faixa_tot, x="Faixa Etária", y="Nº de Casos",
        color="Nº de Casos", color_continuous_scale=[PCOLOR[-1], PCOLOR[0]],
        text="Nº de Casos",
    )
    fig6.update_traces(textposition="outside", textfont_size=10)
    fig6.update_xaxes(tickangle=-30)
    fig_layout(fig6, "Casos por Faixa Etária")
    fig6.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig6, use_container_width=True)

with col_agr:
    agr_tot = (
        df.groupby("Perfil do Agressor")["Nº de Casos"].sum()
          .reset_index()
          .sort_values("Nº de Casos")
    )
    fig7 = px.bar(
        agr_tot, x="Nº de Casos", y="Perfil do Agressor", orientation="h",
        color="Nº de Casos", color_continuous_scale=[PCOLOR[-1], PCOLOR[0]],
        text="Nº de Casos",
    )
    fig7.update_traces(textposition="outside", textfont_size=10)
    fig_layout(fig7, "Perfil do Agressor")
    fig7.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig7, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════
# 13. SEÇÃO 4 – TABELA DETALHADA
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Dados Detalhados</div>', unsafe_allow_html=True)

with st.expander("Ver tabela de dados filtrados (primeiros 1.000 registros)"):
    st.dataframe(
        df.drop(columns=["Observação"], errors="ignore").head(1000),
        use_container_width=True,
        height=320,
    )
