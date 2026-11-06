# ⚡ E-Commerce Analytics Dashboard

A full-stack analytics platform for an online fashion shop — built with **Streamlit**, **PostgreSQL (Supabase)**, **Plotly**, and **Scikit-Learn**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51+-red?logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo

👉 **[Live Demo](https://ecommerce-analytics-dtzoxjkhruuuufxvn6rvrb.streamlit.app/)** — Login: `admin` / `admin123`

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
[postgres]
user = "postgres.XXXXXXXX"
password = "YOUR_SUPABASE_PASSWORD"
host = "aws-0-eu-central-1.pooler.supabase.com"
port = "6543"
database = "postgres"
sslmode = "require"
```

### 4. Run locally
---
Clone the repository and install dependencies:

  git clone https://github.com/Ramzis5/ecommerce-analytics.git
  cd ecommerce-analytics
  python -m pip install -r requirements.txt

Create .streamlit/secrets.toml with your Supabase connection details:

  [postgres]
   user = "YOUR_DATABASE_USER"
   password = "YOUR_DATABASE_PASSWORD"
   host = "YOUR_DATABASE_HOST"
   port = "6543"
   database = "postgres"
   sslmode = "require"

Use the host, user and port from your Supabase connection settings. Keep secrets.toml out of Git.

Start the app:

    streamlit run DataVita.py

Keep data_runtime.py, ml_reliability.py, export_runtime.py and runtime_diagnostics.py alongside DataVita.py.

## 📁 Project Structure

```
ecommerce-analytics/
├── DataVita.py               # Main application
├── data_runtime.py           # Database-side event aggregates
├── ml_reliability.py         # Cache fingerprints and ML input guards
├── export_runtime.py         # Streaming Excel export
├── runtime_diagnostics.py    # Peak memory markers for Cloud logs
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

> <img width="1724" height="5074" alt="screencapture-ecommerce-analytics-1" src="https://github.com/user-attachments/assets/cd61eba9-ac62-4d05-ba0e-9672c5886689" />

<img width="1366" height="599" alt="screencapture_ecommerce_analytics_2" src="https://github.com/user-attachments/assets/291a9042-7cda-419a-9b85-f8a86568e6ba" />

<img width="1366" height="1297" alt="screencapture-ecommerce-analytics-3" src="https://github.com/user-attachments/assets/7fdc851c-95da-40b5-8e13-63bf7d13f62a" />

<img width="1366" height="3246" alt="screencapture-ecommerce-analytics-7" src="https://github.com/user-attachments/assets/1d8c4fb7-705b-420e-9eff-94f1aab63a56" />
<img width="1366" height="599" alt="screencapture_1793978462137" src="https://github.com/user-attachments/assets/cd02efbe-5ff9-4bfc-9b9b-ea5c040e74c9" />
<img width="1365" height="588" alt="screencapture_1793978766394" src="https://github.com/user-attachments/assets/ac374fc4-4f16-4619-bc77-9fc7d6ff7177" />
<img width="1364" height="591" alt="screencapture_1793978889543" src="https://github.com/user-attachments/assets/db503b07-8554-4a6f-b741-3e379925134e" />

---

## 👤 Author

**Ramzi Amara**
- Abschlussprojekt · Data Science · Weiterbildung 2026
- GitHub: [Ramzis5](https://github.com/Ramzis5)

---

## 📄 License

This project is licensed under the MIT License.
