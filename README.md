# NEXTBUY

Système de prédiction de rachat de produits : un dashboard interactif construit avec Streamlit et XGBoost.

## Présentation

NEXTBUY est un outil d'aide à la décision qui prédit la probabilité qu'un client rachète un produit lors de sa prochaine commande, à partir de son historique d'achats et des informations produit.

Le projet s'appuie sur des données issues de millions de commandes alimentaires du dataset Instacart.

## Fonctionnalités

* **Prédiction de rachat** : prédictions en temps réel avec un modèle XGBoost entraîné sur 10 variables client, produit et commande
* **Meilleures ventes** : visualisation des 10 produits les plus commandés
* **Explications** : explications textuelles pour chaque prédiction et analyse SHAP dans le notebook

## Stack technique

| Composant           | Technologie                    |
| ------------------- | ------------------------------ |
| Dashboard           | Streamlit                      |
| Modèle              | XGBoost                        |
| Analyse de données  | Pandas, NumPy, Seaborn, Plotly |
| Explicabilité       | SHAP                           |
| Conteneurisation    | Docker                         |

## Structure du projet

```text
Nextbuy/
├── dashboard.py          # Page d'accueil Streamlit
├── pages/
│   ├── prediction.py     # Page de prédiction interactive
│   └── bestsellers.py    # Top 10 des produits les plus commandés
├── notebook.ipynb        # Analyse des données et entraînement du modèle
├── Dockerfile            # Image Docker pour le déploiement
├── .dockerignore         # Fichiers exclus du build Docker
├── requirements.txt      # Dépendances Python
├── .gitignore
│
├── datasets/             # (non inclus) Fichiers CSV Instacart
│   ├── orders.csv
│   ├── order_products.csv
│   ├── products.csv
│   ├── aisles.csv
│   └── departments.csv
│
└── artifacts/            # (non inclus) Modèle entraîné
    └── model.pkl
```

> `datasets/` et `artifacts/` ne sont pas inclus dans le dépôt car ils sont trop volumineux ou générés localement.

## Installation

### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lancer l'application

```bash
streamlit run dashboard.py
```

L'application est accessible à l'adresse :

`http://localhost:8501`

## Docker

```bash
# Construire l'image
docker build -t nextbuy .

# Lancer le conteneur
docker run -p 8501:8501 nextbuy
```

L'application est accessible à l'adresse :

`http://localhost:8501`

## Modèle

Le modèle XGBoost est entraîné dans `notebook.ipynb` à partir des 10 variables suivantes :

| Variable                 | Description                             |
| ------------------------ | --------------------------------------- |
| `prod_reorder_rate`      | Taux de rachat historique du produit    |
| `add_to_cart_order`      | Position du produit dans le panier      |
| `nb_commandes`           | Nombre total de commandes du client     |
| `panier_moy`             | Taille moyenne du panier                |
| `delai_moyen`            | Délai moyen entre deux commandes (jours)|
| `days_since_prior_order` | Jours depuis la commande précédente     |
| `order_number`           | Numéro de la commande en cours          |
| `prod_nb_orders`         | Popularité du produit                   |
| `order_dow`              | Jour de la semaine                      |
| `order_hour_of_day`      | Heure de la commande                    |

---

Ce projet a été réalisé dans le cadre de ma formation à Epitech.
