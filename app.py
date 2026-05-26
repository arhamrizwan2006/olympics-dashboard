import streamlit as st
from filters import load_data, apply_filters
import charts

st.set_page_config(page_title="Olympics Explorer", page_icon="🏅", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

/* ── MAIN BACKGROUND ── */
.stApp {
    background: linear-gradient(160deg, #0d1117 0%, #0d1b2a 50%, #1a1a2e 100%);
}
.block-container {
    background: transparent !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #161b22 100%);
    border-right: 1px solid rgba(255,255,255,0.07);
}
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stTextInput label {
    color: #8b949e !important;
    font-size: 0.72rem !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
[data-testid="stSidebar"] h3 {
    color: white !important;
    font-size: 1rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 0.5rem;
}
.stButton > button {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.15);
    color: white !important;
    width: 100%;
    border-radius: 6px;
    font-size: 0.8rem;
}
.stButton > button:hover {
    background: rgba(255,255,255,0.1);
}

/* ── HEADER ── */
.main-header {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    padding: 3rem 2.5rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(102,126,234,0.2);
}
.main-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(102,126,234,0.25) 0%, transparent 70%);
    border-radius: 50%;
}
.header-badge {
    display: inline-block;
    background: rgba(102,126,234,0.2);
    border: 1px solid rgba(102,126,234,0.4);
    color: #a78bfa !important;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    margin-bottom: 1rem;
}
.header-title {
    font-size: 2.8rem;
    font-weight: 800;
    color: white !important;
    margin: 0.5rem 0;
    line-height: 1.1;
    letter-spacing: -0.02em;
}
.header-title span {
    background: linear-gradient(90deg, #667eea, #f093fb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.header-sub {
    color: rgba(255,255,255,0.5) !important;
    font-size: 0.9rem;
    margin-top: 0.8rem;
}
.header-stats {
    display: flex;
    gap: 2rem;
    margin-top: 1.5rem;
}
.header-stat {
    color: rgba(255,255,255,0.4) !important;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
.header-stat strong {
    display: block;
    color: white !important;
    font-size: 1.1rem;
    font-weight: 700;
}

/* ── KPI CARDS ── */
.kpi-card-blue {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(102,126,234,0.35);
    border: 1px solid rgba(102,126,234,0.3);
}
.kpi-card-orange {
    background: linear-gradient(135deg, #f093fb, #f5576c);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(245,87,108,0.35);
}
.kpi-card-green {
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(79,172,254,0.35);
}
.kpi-card-yellow {
    background: linear-gradient(135deg, #43e97b, #38f9d7);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(67,233,123,0.35);
}
.kpi-number {
    font-size: 2rem;
    font-weight: 800;
    margin: 0;
    color: white;
}
.kpi-label {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    opacity: 0.85;
    margin: 0 0 0.3rem 0;
    color: white;
}

/* ── CHART CONTAINERS ── */
.chart-container {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 4px 24px rgba(0,0,0,0.3);
}
.chart-title {
    font-size: 1rem;
    font-weight: 700;
    color: white !important;
    margin-bottom: 0.2rem;
}
.chart-desc {
    font-size: 0.78rem;
    color: #8b949e !important;
    margin-bottom: 1rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.chart-number {
    display: inline-block;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    font-size: 0.62rem;
    font-weight: 700;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    text-align: center;
    line-height: 20px;
    margin-right: 0.5rem;
}

/* ── SECTION HEADERS ── */
.section-header {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: #8b949e;
    font-weight: 700;
    margin: 2rem 0 1rem 0;
    padding-left: 0.8rem;
    border-left: 3px solid #667eea;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 4px;
    border: 1px solid rgba(255,255,255,0.08);
    gap: 2px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 7px;
    padding: 0.5rem 1.2rem;
    font-size: 0.82rem;
    font-weight: 500;
    color: #8b949e !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(102,126,234,0.2) !important;
    color: white !important;
    font-weight: 600 !important;
    border: 1px solid rgba(102,126,234,0.3) !important;
}

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* ── GENERAL TEXT ── */
p, span, div, h1, h2, h3, h4 {
    color: rgba(255,255,255,0.85);
}

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("### ⚙️ Filter Data")
    season = st.selectbox("Season", ['All', 'Summer', 'Winter'])
    year_range = st.slider("Year Range",
        int(df['Year'].min()), int(df['Year'].max()),
        (int(df['Year'].min()), int(df['Year'].max())))
    sex = st.selectbox("Sex", ['All', 'M', 'F'])
    sports = st.multiselect("Sport",
        sorted(df['Sport'].unique()),
        placeholder="All sports")
    search = st.text_input("Search Athlete")
    st.markdown("---")
    if st.button("↺  Reset All Filters"):
        st.rerun()

filtered_df = apply_filters(df, season, year_range, sex, sports, search)

# ── HEADER ──
st.markdown(f"""
<div class="main-header">
    <div class="header-badge">🏅 Data Visualization Dashboard</div>
    <div class="header-title">Olympic Athletes<br><span>120 Years</span> of History</div>
    <div class="header-sub">Exploring every athlete, medal and sport from Athens 1896 to Rio 2016</div>
    <div class="header-stats">
        <div class="header-stat"><strong>{len(df):,}</strong> Total Records</div>
        <div class="header-stat"><strong>120</strong> Years of Data</div>
        <div class="header-stat"><strong>50+</strong> Sports</div>
        <div class="header-stat"><strong>213</strong> Countries</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── KPI CARDS ──
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f"""<div class="kpi-card-blue">
        <p class="kpi-label">Filtered Records</p>
        <p class="kpi-number">{len(filtered_df):,}</p>
    </div>""", unsafe_allow_html=True)
with k2:
    st.markdown(f"""<div class="kpi-card-orange">
        <p class="kpi-label">Average Age</p>
        <p class="kpi-number">{filtered_df['Age'].mean():.1f}</p>
    </div>""", unsafe_allow_html=True)
with k3:
    st.markdown(f"""<div class="kpi-card-green">
        <p class="kpi-label">Medals Awarded</p>
        <p class="kpi-number">{len(filtered_df[filtered_df['Medal']!='No Medal']):,}</p>
    </div>""", unsafe_allow_html=True)
with k4:
    st.markdown(f"""<div class="kpi-card-yellow">
        <p class="kpi-label">Countries</p>
        <p class="kpi-number">{filtered_df['region'].nunique()}</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── TABS ──
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Distribution", "📈 Trends", "🔬 Relationships", "🏆 Leaderboard", "⭐ Bonus"
])

# ── TAB 1: Distribution (Pie, Histogram, Count Plot) ──
with tab1:
    st.markdown('<p class="section-header">Proportional & Frequency Analysis</p>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">1</span>Medal Distribution</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Proportional distribution of Gold, Silver and Bronze medals</p>', unsafe_allow_html=True)
    st.pyplot(charts.pie_chart(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">2</span>Age Distribution</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Frequency distribution of athlete ages across all Olympics</p>', unsafe_allow_html=True)
    st.pyplot(charts.histogram(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">9</span>Male vs Female Athletes</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Frequency count of male and female participation</p>', unsafe_allow_html=True)
    st.pyplot(charts.count_plot(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

# ── TAB 2: Trends (Line, Bar, Area) ──
with tab2:
    st.markdown('<p class="section-header">Trends Over Time & Categories</p>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">3</span>Athletes Over the Years</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Trend of Olympic participation from 1896 to 2016</p>', unsafe_allow_html=True)
    st.pyplot(charts.line_chart(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">4</span>Top 10 Countries by Medals</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Comparing medal counts across top performing nations</p>', unsafe_allow_html=True)
    st.pyplot(charts.bar_chart(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">8</span>Sports Over the Years</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Cumulative growth of sports disciplines over time</p>', unsafe_allow_html=True)
    st.pyplot(charts.area_chart(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

# ── TAB 3: Relationships (Scatter, Box, Heatmap, Violin) ──
with tab3:
    st.markdown('<p class="section-header">Statistical Relationships & Distributions</p>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">5</span>Height vs Weight</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Relationship between two numerical variables — height and weight</p>', unsafe_allow_html=True)
    st.pyplot(charts.scatter_plot(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">6</span>Age by Medal Type</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Data spread, median and outliers of age across medal categories</p>', unsafe_allow_html=True)
    st.pyplot(charts.box_plot(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">7</span>Correlation Heatmap</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Correlation matrix between Age, Height and Weight</p>', unsafe_allow_html=True)
    st.pyplot(charts.heatmap(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title"><span class="chart-number">10</span>Age by Season</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Distribution and probability density of age in Summer vs Winter</p>', unsafe_allow_html=True)
    st.pyplot(charts.violin_plot(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

# ── TAB 4: LEADERBOARD ──
with tab4:
    st.markdown('<p class="section-header">Medal Table</p>', unsafe_allow_html=True)

    medal_df = filtered_df[filtered_df['Medal'] != 'No Medal']
    country_medals = medal_df.groupby('region')['Medal'].value_counts().unstack(fill_value=0)
    for col in ['Gold', 'Silver', 'Bronze']:
        if col not in country_medals.columns:
            country_medals[col] = 0
    country_medals['Total'] = country_medals['Gold'] + country_medals['Silver'] + country_medals['Bronze']
    country_medals = country_medals.sort_values('Total', ascending=False).head(20).reset_index()
    country_medals.index += 1

    flag_map = {
        'USA': '🇺🇸', 'Russia': '🇷🇺', 'Germany': '🇩🇪', 'UK': '🇬🇧',
        'France': '🇫🇷', 'Italy': '🇮🇹', 'Sweden': '🇸🇪', 'Australia': '🇦🇺',
        'Hungary': '🇭🇺', 'China': '🇨🇳', 'Norway': '🇳🇴', 'Finland': '🇫🇮',
        'Japan': '🇯🇵', 'Romania': '🇷🇴', 'Netherlands': '🇳🇱', 'Cuba': '🇨🇺',
        'Canada': '🇨🇦', 'South Korea': '🇰🇷', 'Poland': '🇵🇱', 'Denmark': '🇩🇰'
    }

    country_medals['Country'] = country_medals['region'].apply(
        lambda x: flag_map.get(x, '🏳️') + ' ' + x)
    display_df = country_medals[['Country', 'Gold', 'Silver', 'Bronze', 'Total']]
    display_df.columns = ['Country', '🥇 Gold', '🥈 Silver', '🥉 Bronze', 'Total']
    st.dataframe(display_df, use_container_width=True, height=500)

    st.markdown('<p class="section-header">Top Individual Athletes</p>', unsafe_allow_html=True)
    top_athletes = medal_df.groupby(['Name', 'region', 'Sport'])['Medal'].count().reset_index()
    top_athletes.columns = ['Athlete', 'Country', 'Sport', 'Medals']
    top_athletes = top_athletes.sort_values('Medals', ascending=False).head(15).reset_index(drop=True)
    top_athletes.index += 1
    top_athletes['Country'] = top_athletes['Country'].apply(
        lambda x: flag_map.get(x, '🏳️') + ' ' + x)
    st.dataframe(top_athletes, use_container_width=True, height=400)

# ── TAB 5: BONUS ──
with tab5:
    st.markdown('<p class="section-header">Bonus Visualizations</p>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title">✦ Pair Plot — Physical Attributes</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Relationships between Age, Height and Weight split by gender</p>', unsafe_allow_html=True)
    st.pyplot(charts.pair_plot(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title">✦ Bubble Chart — Countries</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">Bubble size represents total medals. Top 10 countries labeled.</p>', unsafe_allow_html=True)
    st.pyplot(charts.bubble_chart(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<p class="chart-title">✦ Funnel Chart — Participation to Gold</p>', unsafe_allow_html=True)
    st.markdown('<p class="chart-desc">How many athletes make it from participation all the way to Gold</p>', unsafe_allow_html=True)
    st.pyplot(charts.funnel_chart(filtered_df))
    st.markdown('</div>', unsafe_allow_html=True)