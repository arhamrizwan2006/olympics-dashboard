# 🏅 120 Years of Olympic Athletes Dashboard

**Course:** Exploratory Data Analysis  
**Instructor:** Ali Hassan Sherazi

🔗 **Live Demo:** [olympics-dashboard-arham.streamlit.app](https://olympics-dashboard-arham.streamlit.app)

## Project Overview
An interactive data visualization dashboard analyzing 120 years of Olympic history 
(1896–2016), covering athletes, medals, sports, and countries. Built with Python, 
Pandas, Seaborn, Matplotlib, and deployed live using Streamlit.

## Dataset
- `athlete_events.csv` — main dataset with athlete information
- `noc_regions.csv` — country/region mapping

## Tech Stack
| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas / NumPy | Data cleaning and analysis |
| Matplotlib / Seaborn | Static visualizations |
| Streamlit | Interactive dashboard & deployment |

## How to Run Locally
```
pip install pandas numpy matplotlib seaborn streamlit
cd Downloads\Dashboard
python -m streamlit run app.py
```
Dashboard opens automatically in browser at `localhost:8501`

## Key Insights
- 271,116 total athlete records across 120 years
- 213 countries participated in Olympic history
- Average athlete age is 25.5 years
- USA, Russia, and Germany are the top medal-winning countries
- Male athletes outnumber female athletes historically
- Summer Olympics has significantly more participants than Winter
- Height and weight show a strong positive correlation

## Charts Included
1. Pie Chart — Medal Distribution
2. Histogram — Age Distribution
3. Line Chart — Athletes Over Years
4. Bar Chart — Top 10 Countries
5. Scatter Plot — Height vs Weight
6. Box Plot — Age by Medal Type
7. Heatmap — Correlation Matrix
8. Area Chart — Sports Over Years
9. Count Plot — Male vs Female
10. Violin Plot — Age by Season

## Project Structure
```
dashboard_project/
├── data/
│   ├── athlete_events.csv
│   └── noc_regions.csv
├── notebooks/
│   └── analysis.ipynb
├── app.py
├── charts.py
├── filters.py
├── requirements.txt
└── README.md
```

## What I Learned
- Exploratory data analysis on a large historical dataset
- Building interactive filters and dashboards with Streamlit
- Choosing effective chart types for different kinds of insights
- Deploying a Python data app publicly via Streamlit Cloud