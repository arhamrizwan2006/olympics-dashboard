import streamlit as st
from filters import load_data, apply_filters
import charts

st.set_page_config(page_title="Olympics Dashboard", page_icon="🏅", layout="wide")

@st.cache_data
def get_data():
    return load_data()

df = get_data()

st.title("🏅 120 Years of Olympic Athletes Dashboard")
st.markdown("Exploring Olympic data from **1896 to 2016** — athletes, medals, sports and more.")
st.markdown("---")

# ── SIDEBAR ──
st.sidebar.title("🔍 Filters")
season = st.sidebar.selectbox("Season", ['All', 'Summer', 'Winter'])
year_range = st.sidebar.slider("Year Range",
    int(df['Year'].min()), int(df['Year'].max()),
    (int(df['Year'].min()), int(df['Year'].max())))
sex = st.sidebar.selectbox("Sex", ['All', 'M', 'F'])
sports = st.sidebar.multiselect("Sports", sorted(df['Sport'].unique()))
search = st.sidebar.text_input("Search Athlete Name")
st.sidebar.markdown("---")
if st.sidebar.button("🔄 Reset Filters"):
    st.rerun()

filtered_df = apply_filters(df, season, year_range, sex, sports, search)

# ── KPI CARDS ──
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", f"{len(filtered_df):,}")
col2.metric("Average Age", f"{filtered_df['Age'].mean():.1f}")
col3.metric("Total Medals", f"{len(filtered_df[filtered_df['Medal']!='No Medal']):,}")
col4.metric("Countries", f"{filtered_df['region'].nunique()}")
st.markdown("---")

# ── TABS ──
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🌍 Countries & Medals", "👤 Athletes", "🏆 Leaderboard"])

# ── TAB 1 ──
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🥇 Medal Distribution")
        st.pyplot(charts.pie_chart(filtered_df))
        st.caption("Gold, Silver and Bronze medals are fairly evenly distributed across all Olympics.")

    with col2:
        st.subheader("📊 Age Distribution")
        st.pyplot(charts.histogram(filtered_df))
        st.caption("Most Olympic athletes are between 20 and 30 years old.")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("📈 Athletes Over the Years")
        st.pyplot(charts.line_chart(filtered_df))
        st.caption("Participation grew steadily, with a major increase after the 1980s as more nations joined.")

    with col4:
        st.subheader("🏃 Sports Over the Years")
        st.pyplot(charts.area_chart(filtered_df))
        st.caption("The number of sports has expanded significantly, especially in Summer Olympics.")

# ── TAB 2 ──
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌍 Top 10 Countries by Medals")
        st.pyplot(charts.bar_chart(filtered_df))
        st.caption("USA, Russia and Germany have historically dominated the Olympic medal tally.")

    with col2:
        st.subheader("🔥 Correlation Heatmap")
        st.pyplot(charts.heatmap(filtered_df))
        st.caption("Height and Weight show a strong positive correlation among athletes.")

# ── TAB 3 ──
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚖️ Height vs Weight")
        st.pyplot(charts.scatter_plot(filtered_df))
        st.caption("Clear difference in body composition between male and female athletes.")

    with col2:
        st.subheader("👥 Male vs Female Athletes")
        st.pyplot(charts.count_plot(filtered_df))
        st.caption("Female participation has grown dramatically since the early 1900s.")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("🎯 Age by Medal Type")
        st.pyplot(charts.box_plot(filtered_df))
        st.caption("Medal winners tend to cluster around ages 22 to 28 across all medal types.")

    with col4:
        st.subheader("🎻 Age by Season")
        st.pyplot(charts.violin_plot(filtered_df))
        st.caption("Winter Olympic athletes tend to be slightly older on average than Summer athletes.")

# ── TAB 4: LEADERBOARD ──
with tab4:
    st.subheader("🥇 Top Medal Winning Countries")

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
        lambda x: flag_map.get(x, '🏳️') + ' ' + x
    )
    display_df = country_medals[['Country', 'Gold', 'Silver', 'Bronze', 'Total']]
    display_df.columns = ['Country', '🥇 Gold', '🥈 Silver', '🥉 Bronze', 'Total']
    st.dataframe(display_df, use_container_width=True, height=500)

    st.markdown("---")
    st.subheader("🏅 Top Individual Athletes by Medals")

    top_athletes = medal_df.groupby(['Name', 'region', 'Sport'])['Medal'].count().reset_index()
    top_athletes.columns = ['Athlete', 'Country', 'Sport', 'Medals']
    top_athletes = top_athletes.sort_values('Medals', ascending=False).head(15).reset_index(drop=True)
    top_athletes.index += 1
    top_athletes['Country'] = top_athletes['Country'].apply(
        lambda x: flag_map.get(x, '🏳️') + ' ' + x
    )
    st.dataframe(top_athletes, use_container_width=True, height=400)