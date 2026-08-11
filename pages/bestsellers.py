import streamlit as st
import pandas as pd
import os
import altair as alt

st.title("Produits bestsellers")
st.caption("Top 10 des produits les plus commandés")
st.write(
    "Ces produits apparaissent dans le top 10 car ils sont les plus fréquemment commandés, "
    "calculés avec `value_counts` sur `product_name` (Q3)."
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "datasets")
order_products_path = os.path.join(DATA_DIR, "order_products.csv")
products_path = os.path.join(DATA_DIR, "products.csv")

order_products = pd.read_csv(order_products_path, usecols=["product_id"])
products = pd.read_csv(products_path, usecols=["product_id", "product_name"])
merged = order_products.merge(products, on="product_id")

counts = merged["product_name"].value_counts()
top10 = counts.head(10).reset_index()
top10.columns = ["product_name", "orders"]
top10 = top10.sort_values("orders", ascending=True)

chart = alt.Chart(top10).mark_bar(color="#4CAF50").encode(
    x=alt.X("orders", title="Nombre de commandes"),
    y=alt.Y(
        "product_name",
        sort=alt.EncodingSortField(field="orders", order="descending"),
        title="Produit"
    ),
    tooltip=["product_name", "orders"]
).properties(height=400)

st.altair_chart(chart, use_container_width=True)