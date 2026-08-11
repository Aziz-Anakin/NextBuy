import streamlit as st

st.set_page_config(page_title="NEXTBUY", layout="centered")

st.markdown("# NEXTBUY")
st.markdown("##### Système de prédiction de rachat produit")

st.divider()

st.markdown("""
**NEXTBUY** est un outil d'aide à la décision pour anticiper le comportement d'achat des clients.

À partir du profil client et des caractéristiques d'un produit, le modèle estime la probabilité
que ce client rachete ce produit lors de sa prochaine commande.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Features**")
    st.markdown("### 10")
    st.caption(
        "Les variables résument le contexte client/commande/produit : "
        "c'est ce que le modèle utilise pour prendre sa décision."
    )

with col2:
    st.markdown("**Modèle**")
    st.markdown("### XGBoost")
    st.caption(
        "Bon compromis performance/robustesse sur des données tabulaires, "
        "et rapide à utiliser dans un dashboard."
    )

with col3:
    st.markdown("**Tâche**")
    st.markdown("### Classification")
    st.caption(
        "Le but est d'estimer une probabilité de rachat : ça aide à prioriser les produits à recommander."
    )
