# NEXTBUY

Product repurchase prediction system — an interactive dashboard built with Streamlit and XGBoost.

## Overview

NEXTBUY is a decision-support tool that predicts the probability of a customer buying a product again in their next order, based on customer history and product information.

The project uses data from millions of grocery orders from the Instacart dataset.

## Features

* **Repurchase Prediction**: real-time predictions using an XGBoost model trained on 10 customer, product, and order features
* **Bestsellers**: visualization of the 10 most ordered products
* **Explanations**: text explanations for each prediction and SHAP analysis in the notebook

## Tech Stack

| Component        | Technology                     |
| ---------------- | ------------------------------ |
| Dashboard        | Streamlit                      |
| Model            | XGBoost                        |
| Data Analysis    | Pandas, NumPy, Seaborn, Plotly |
| Explainability   | SHAP                           |
| Containerization | Docker                         |

## Project Structure

```text
Nextbuy/
├── dashboard.py          # Streamlit home page
├── pages/
│   ├── prediction.py     # Interactive prediction page
│   └── bestsellers.py    # Top 10 most ordered products
├── notebook.ipynb        # Data analysis and model training
├── Dockerfile            # Docker image for deployment
├── .dockerignore         # Files excluded from Docker build
├── requirements.txt      # Python dependencies
├── .gitignore
│
├── datasets/             # (not included) Instacart CSV files
│   ├── orders.csv
│   ├── order_products.csv
│   ├── products.csv
│   ├── aisles.csv
│   └── departments.csv
│
└── artifacts/            # (not included) Trained model
    └── model.pkl
```

> `datasets/` and `artifacts/` are not included in the repository because they are too large or generated locally.

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

## Run the Application

```bash
streamlit run dashboard.py
```

The application will be available at:

`http://localhost:8501`

## Docker

```bash
# Build the image
docker build -t nextbuy .

# Run the container
docker run -p 8501:8501 nextbuy
```

The application will be available at:

`http://localhost:8501`

## Model

The XGBoost model is trained in `notebook.ipynb` using the following 10 features:

| Feature                  | Description                        |
| ------------------------ | ---------------------------------- |
| `prod_reorder_rate`      | Historical product reorder rate    |
| `add_to_cart_order`      | Product position in the cart       |
| `nb_commandes`           | Total number of customer orders    |
| `panier_moy`             | Average cart size                  |
| `delai_moyen`            | Average time between orders (days) |
| `days_since_prior_order` | Days since the previous order      |
| `order_number`           | Current order number               |
| `prod_nb_orders`         | Product popularity                 |
| `order_dow`              | Day of the week                    |
| `order_hour_of_day`      | Order time (hour)                  |

```
```
