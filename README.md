# ⚡ E-Commerce Analytics Dashboard

A full-stack analytics platform for an online fashion shop — built with **Streamlit**, **PostgreSQL (Supabase)**, **Plotly**, and **Scikit-Learn**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red?logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo

👉 **[Live Demo](https://ecommerce-analytics-ijhsnlmvkbnu7pudhbjviz.streamlit.app)** — Login: `admin` / `admin123`

---

## 📊 Features

### BI Dashboard (5 Analysis Pages)
- **Executive Overview** — Revenue, orders, profit KPIs with trend analysis
- **Customer & Conversion** — Funnel analysis, demographics, traffic sources
- **Product & Inventory** — Top products, category performance, brand analysis
- **Return Analysis** — Return rates, reasons, patterns
- **Advanced Insights** — Deep-dive analytics with custom filters

### Machine Learning
- **Churn Prediction** — Random Forest & Gradient Boosting with SMOTE balancing
- **Sales Forecasting** — Linear Regression with trend analysis

### Customer Intelligence
- **RFM Segmentation** — Recency, Frequency, Monetary customer scoring

### Extras
- **Export & Reports** — CSV/Excel export functionality
- **20+ Interactive Charts** — Plotly-powered visualizations
- **Dark Theme UI** — Custom CSS premium design
- **Multi-page Navigation** — Sidebar with filter pipeline

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit, Custom CSS, Plotly |
| Backend | Python, Pandas, NumPy |
| Database | PostgreSQL (Supabase) |
| ML | Scikit-Learn, Imbalanced-Learn |
| Deployment | Streamlit Cloud |

---

## 📦 Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/Ramzis5/ecommerce-analytics.git
cd ecommerce-analytics
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure secrets
Create `.streamlit/secrets.toml`:
```toml
[database]
user = "postgres.XXXXXXXX"
password = "YOUR_SUPABASE_PASSWORD"
host = "aws-0-eu-central-1.pooler.supabase.com"
port = "6543"
name = "postgres"

[auth]
username = "admin"
password = "admin123"
```

### 4. Run locally
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
ecommerce-analytics/
├── app.py                    # Main application (4800+ lines)
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── .streamlit/
│   ├── config.toml          # Streamlit theme config
│   └── secrets.toml         # Database credentials (NOT in git)
└── README.md
```

---

## 🗄️ Database Schema

The app queries 5 PostgreSQL tables:

- `order_items` — Sales transactions
- `product` — Product catalog
- `users` — Customer data
- `events` — User behavior tracking
- `distribution_centers` — Warehouse locations

Data source: **TheLook E-Commerce** dataset (100K+ records)

---

## 📸 Screenshots

> _Add screenshots of your dashboard here_

---

## 👤 Author

**Ramzi Amara**
- Abschlussprojekt · Data Science · Weiterbildung 2026
- GitHub: [Ramzis5](https://github.com/Ramzis5)

---

## 📄 License

This project is licensed under the MIT License.
