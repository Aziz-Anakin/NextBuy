import streamlit as st
import pandas as pd
import joblib
import os

st.title("Prediction de rachat")
st.caption("Estimez la probabilite qu'un client rachete un produit")

with st.expander("Parametres client", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        nb_commandes = st.slider("Commandes", 1, 100, 10, help="Nombre total de commandes du client")
        panier_moy = st.slider("Panier moyen", 1, 50, 8, help="Taille moyenne du panier")
        order_number = st.slider("Numero de commande", 1, 100, 10, help="Numero de la commande en cours")
    with col2:
        delai_moyen = st.slider("Delai moyen (j)", 1, 30, 11, help="Delai entre commandes")
        jours_depuis = st.slider("Jours depuis derniere cmd", 1, 30, 11, help="Temps ecoule depuis la derniere commande")

with st.expander("Parametres produit", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        taux_rachat = st.slider("Taux de rachat produit", 0.0, 1.0, 0.5, help="Historique de rachat de ce produit")
        popularite = st.slider("Popularite", 100, 50000, 5000, help="Nombre de commandes du produit")
    with col2:
        position_panier = st.slider("Position panier", 1, 30, 5, help="Ordre d'ajout au panier")

with st.expander("Parametres commande", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        order_dow = st.slider("Jour de la semaine (0=lundi)", 0, 6, 0)
    with col2:
        order_hour = st.slider("Heure de la commande", 0, 23, 12)

if st.button("Predire", type="primary", use_container_width=True):
    data = pd.DataFrame([{
        "order_dow": order_dow,
        "order_hour_of_day": order_hour,
        "days_since_prior_order": jours_depuis,
        "add_to_cart_order": position_panier,
        "order_number": order_number,
        "nb_commandes": nb_commandes,
        "panier_moy": panier_moy,
        "delai_moyen": delai_moyen,
        "prod_reorder_rate": taux_rachat,
        "prod_nb_orders": popularite,
    }])

    try:
        model_path = os.path.join(os.path.dirname(__file__), "..", "artifacts", "model.pkl")
        model = joblib.load(model_path)
        proba = float(model.predict_proba(data)[0, 1])
    except Exception as e:
        st.error(f"Erreur chargement modele : {e}")
        proba = (
            taux_rachat * 0.55
            + (1 / position_panier) * 0.20
            + min(nb_commandes / 100, 1) * 0.15
            + max(0, 1 - jours_depuis / 30) * 0.10
        )
        proba = min(max(proba, 0), 1)
        st.info("Prediction heuristique utilisee")

    st.divider()

    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Probabilite", f"{proba * 100:.0f}%")
    with col2:
        st.progress(float(proba))

    if proba >= 0.7:
        st.success("Rachat probable")
    elif proba >= 0.45:
        st.warning("Rachat incertain")
    else:
        st.error("Rachat peu probable")

    st.subheader("Pourquoi cette prediction ?")
    justifications = []

    if taux_rachat >= 0.7:
        justifications.append("Ce produit est souvent rachete par les clients")
    elif taux_rachat <= 0.3:
        justifications.append("Ce produit est rarement rachete")

    if position_panier <= 3:
        justifications.append("Le client l'a ajoute en debut de panier = prioritaire")
    elif position_panier >= 15:
        justifications.append("Ajoute tardivement = moins prioritaire")

    if nb_commandes >= 30:
        justifications.append("Client fidélisé avec beaucoup d'achats")
    elif nb_commandes <= 5:
        justifications.append("Nouveau client avec peu d'historique")

    if jours_depuis <= 5:
        justifications.append("Le client vient de commander recemment")
    elif jours_depuis >= 20:
        justifications.append("Temps long depuis derniere commande")

    if popularite >= 20000:
        justifications.append("Produit tres populaire et en demande")

    if panier_moy >= 15:
        justifications.append("Client avec gros panier habituellement")
    elif panier_moy <= 5:
        justifications.append("Client avec petits paniers habituellement")

    if delai_moyen <= 7:
        justifications.append("Client commande tres regulierement")
    elif delai_moyen >= 20:
        justifications.append("Client espace ses commandes")

    for msg in justifications:
        st.caption(f"• {msg}")