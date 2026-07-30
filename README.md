# 🏅 Olympics Data Analysis Dashboard

> 120 years of Olympic history visualized with interactive filters  
> **Live:** https://olympics-dashboard-arham.streamlit.app/  
> **Data:** 1896–2016 | **Framework:** Streamlit | **Built With:** Python

![Badge](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=flat-square)
![Badge](https://img.shields.io/badge/Data-120%20Years-4CAF50?style=flat-square)
![Badge](https://img.shields.io/badge/Visualizations-10%2B%20Charts-2196F3?style=flat-square)

---

## 🎯 What It Shows

```
Raw Olympics Data (1896–2016)
         ↓
   [Clean & Process]
         ↓
   [10+ Interactive Charts]
         ↓
   [6 Dynamic Filters]
         ↓
Live Dashboard
```

Explore medal trends, athlete stats, country performance, and historical patterns across 13 Olympic Games.

---

## 📊 Features

- **10+ Visualizations:** Medal counts, athlete distribution, country dominance, gender trends
- **6 Interactive Filters:** Country, sport, year range, gender, medal type
- **Live Data Exploration:** All charts update instantly based on filters
- **Responsive Design:** Works on desktop, tablet, mobile

---

## 📈 Key Charts

| Chart | Insight |
|-------|---------|
| **Medal Distribution** | Which countries dominate? |
| **Sport Participation** | Most popular Olympic sports |
| **Gender Trends** | Female athlete growth over time |
| **Athlete Statistics** | Age, height, weight patterns |
| **Country Performance** | Medal per capita analysis |

---

## 🚀 Access the Dashboard

**Live:** [olympics-dashboard-arham.streamlit.app](https://olympics-dashboard-arham.streamlit.app/)

No installation needed — view directly in browser. Filters update all charts in real-time.

---

## 💻 Local Setup

```bash
git clone https://github.com/arhamrizwan2006/olympics-dashboard.git
cd olympics-dashboard

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

**Open:** `http://localhost:8501`

---

## 📁 Structure

```
olympics-dashboard/
├── app.py              (Main Streamlit app)
├── charts.py           (Visualization functions)
├── filters.py          (Filter logic)
├── data/
│   ├── athlete_events.csv      (Raw data)
│   └── noc_regions.csv         (Country mappings)
├── notebooks/
│   └── analysis.ipynb  (EDA & development)
└── requirements.txt
```

---

## 💡 Tech Stack

| Component | Purpose |
|-----------|---------|
| **Streamlit** | Interactive web dashboard |
| **Pandas** | Data processing |
| **Seaborn/Matplotlib** | Visualizations |
| **Python** | Backend logic |

---

## 🎨 Interactive Filters

```
┌─ Country ────────┐
│ ○ All / Select   │
├─ Sport ──────────┤
│ ○ All / Choose   │
├─ Year Range ─────┤
│ 1896 ←→ 2016    │
├─ Gender ─────────┤
│ ○ All/M/F        │
└─ Medal Type ─────┘
   ↓
All charts update
instantly ⚡
```

---

## 📊 Sample Insights

- **🥇 Dominance:** USA leads historically, but China rising
- **📈 Growth:** Female participation increases each Olympics
- **🏃 Sports:** Track & field, swimming most represented
- **🌍 Diversity:** 200+ nations participated across games

---

## 🔧 Data Processing

- **Dataset:** Kaggle Olympics 1896–2016
- **Cleaning:** Handle missing values, standardize country names
- **Aggregation:** Medal counts, athlete statistics
- **Caching:** Streamlit caches for fast interactions

---

**Repo:** [github.com/arhamrizwan2006/olympics-dashboard](https://github.com/arhamrizwan2006/olympics-dashboard)  
**Deployed:** Streamlit Cloud (Auto-updated from main branch)
