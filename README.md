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
```bash
streamlit run DataVita.py
```

---

## 📁 Project Structure

```
ecommerce-analytics/
├── DataVita.py               # Main application
├── data_runtime.py           # Database-side event aggregates
├── ml_reliability.py         # Cache fingerprints and ML input guards
├── export_runtime.py         # Streaming Excel export
├── runtime_diagnostics.py    # Peak memory markers for Cloud logs
├── tests/                    # Offline regression tests
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

## Cloud stability changes

The customer funnel now fetches small SQL aggregates when its page is opened,
instead of keeping the entire raw events table in every session. Distinct
sessions are counted across all selected years; raw event counts retain their
original meaning. The other sidebar filters still apply to sales/customers,
while the event funnel uses the year filter, as before.

Large sales CSV/Excel downloads have a **prepare** button. Excel is written
row by row; timezone-aware dates are exported as UTC without a timezone,
because Excel does not support timezone-aware datetime cells.

Churn caches use complete input fingerprints, keep one entry, and expire.
Random Forest training uses one worker. Forecasting retains at least six
training months when the user changes the date range and test horizon.

Deploy all Python modules together with `DataVita.py` and the updated
`requirements.txt`; keep the Streamlit entrypoint set to `DataVita.py`.
The README's former `[database]` example did not match the code: the app
expects `[postgres]` in Streamlit Secrets. Existing working secrets need no change.

Offline checks (no Supabase credentials needed):

```bash
python -m pip install -r requirements.txt pytest
python -m pytest tests -q
```

Cloud logs include `[runtime] page_start`, `page_end`, and `peak_rss_mib`
markers. The RSS value is the process high-water mark, not current usage.
Use these alongside the platform logs at the time of a crash. The code
contains real memory hotspots, but the generic “Error running app” page alone
does not establish an out-of-memory failure; the live Cloud logs are still
needed to confirm the production cause.

The supplied Cloud log successfully downgraded PyArrow before startup and
contained no actual crash traceback. Requirements now keep the same
`pyarrow<25` compatibility cap explicitly. Native-fault logging is enabled
where supported, and deprecated width arguments have been migrated to `width`.
The offline suite also passes with the main dependency versions in that log
(Streamlit 1.67.0, pandas 3.1.1 and PyArrow 24.0.0).

Existing presentation metrics in the churn page include fixed model scores,
SMOTE counts/status and customer totals. This stability change leaves those
values unchanged; they should not be treated as freshly calculated evaluation
results.

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
