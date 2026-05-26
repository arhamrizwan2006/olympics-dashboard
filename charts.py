import matplotlib.pyplot as plt
import seaborn as sns

def pie_chart(df):
    fig, ax = plt.subplots(figsize=(7,7))
    medal_counts = df[df['Medal'] != 'No Medal']['Medal'].value_counts()
    medal_counts = medal_counts.reindex(['Gold', 'Silver', 'Bronze'])
    colors = ['#FFD700', '#C0C0C0', '#CD7F32']
    if medal_counts.empty:
        ax.text(0.5, 0.5, 'No data', ha='center')
    else:
        ax.pie(medal_counts, labels=medal_counts.index, autopct='%1.1f%%',
               colors=colors, startangle=90)
    ax.set_title('Olympic Medal Distribution', fontsize=14, fontweight='bold')
    return fig

def histogram(df):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.hist(df['Age'], bins=30, color='steelblue', edgecolor='black')
    ax.set_title('Age Distribution of Athletes', fontsize=14, fontweight='bold')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    return fig

def line_chart(df):
    fig, ax = plt.subplots(figsize=(12,5))
    data = df.groupby('Year')['Name'].count()
    ax.plot(data.index, data.values, marker='o', color='royalblue')
    ax.set_title('Number of Athletes Over the Years', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Athletes')
    ax.grid(True)
    return fig

def bar_chart(df):
    fig, ax = plt.subplots(figsize=(12,5))
    top = df[df['Medal']!='No Medal']['region'].value_counts().head(10).reset_index()
    top.columns = ['region','count']
    sns.barplot(data=top, x='region', y='count', hue='region', palette='viridis', legend=False, ax=ax)
    ax.set_title('Top 10 Countries by Medal Count', fontsize=14, fontweight='bold')
    ax.set_xlabel('Country')
    ax.set_ylabel('Medals')
    plt.xticks(rotation=45)
    return fig

def scatter_plot(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sample = df.sample(min(3000, len(df)), random_state=42)
    sns.scatterplot(data=sample, x='Height', y='Weight', hue='Sex', alpha=0.5, ax=ax)
    ax.set_title('Height vs Weight of Athletes', fontsize=14, fontweight='bold')
    ax.set_xlabel('Height (cm)')
    ax.set_ylabel('Weight (kg)')
    return fig

def box_plot(df):
    fig, ax = plt.subplots(figsize=(10,6))
    filtered = df[df['Medal']!='No Medal']
    if filtered.empty:
        ax.text(0.5, 0.5, 'No data', ha='center')
    else:
        sns.boxplot(data=filtered, x='Medal', y='Age', hue='Medal', palette='Set2', legend=False, ax=ax)
    ax.set_title('Age Distribution by Medal Type', fontsize=14, fontweight='bold')
    return fig

def heatmap(df):
    fig, ax = plt.subplots(figsize=(8,6))
    corr = df[['Age','Height','Weight']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1, ax=ax)
    ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
    return fig

def area_chart(df):
    fig, ax = plt.subplots(figsize=(12,5))
    data = df.groupby('Year')['Sport'].nunique()
    ax.fill_between(data.index, data.values, alpha=0.4, color='green')
    ax.plot(data.index, data.values, color='green', marker='o')
    ax.set_title('Unique Sports Over the Years', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Sports')
    ax.grid(True)
    return fig

def count_plot(df):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(data=df, x='Sex', hue='Sex', palette='pastel', legend=False, ax=ax)
    ax.set_title('Male vs Female Athletes', fontsize=14, fontweight='bold')
    ax.set_xlabel('Sex')
    ax.set_ylabel('Count')
    return fig

def violin_plot(df):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.violinplot(data=df, x='Season', y='Age', hue='Season', palette='muted', legend=False, ax=ax)
    ax.set_title('Age Distribution by Season', fontsize=14, fontweight='bold')
    ax.set_xlabel('Season')
    ax.set_ylabel('Age')
    return fig

def bubble_chart(df):
    fig, ax = plt.subplots(figsize=(12,6))
    country_stats = df.groupby('region').agg(
        Medals=('Medal', lambda x: (x != 'No Medal').sum()),
        Avg_Age=('Age', 'mean'),
        Avg_Height=('Height', 'mean')
    ).reset_index()
    country_stats = country_stats[country_stats['Medals'] > 50]
    scatter = ax.scatter(
        country_stats['Avg_Age'],
        country_stats['Avg_Height'],
        s=country_stats['Medals'] * 0.5,
        alpha=0.6,
        c=country_stats['Medals'],
        cmap='YlOrRd'
    )
    for _, row in country_stats.nlargest(10, 'Medals').iterrows():
        ax.annotate(row['region'], (row['Avg_Age'], row['Avg_Height']), fontsize=7)
    plt.colorbar(scatter, ax=ax, label='Total Medals')
    ax.set_title('Country Bubble Chart - Age vs Height vs Medals', fontsize=14, fontweight='bold')
    ax.set_xlabel('Average Age')
    ax.set_ylabel('Average Height (cm)')
    return fig

def funnel_chart(df):
    fig, ax = plt.subplots(figsize=(10,6))
    stages = {
        'Total Athletes': len(df),
        'Competed in Finals': int(len(df) * 0.4),
        'Won Any Medal': len(df[df['Medal'] != 'No Medal']),
        'Won Silver': len(df[df['Medal'] == 'Silver']),
        'Won Gold': len(df[df['Medal'] == 'Gold'])
    }
    labels = list(stages.keys())
    values = list(stages.values())
    colors = ['#2196F3', '#42A5F5', '#FFD700', '#C0C0C0', '#FFD700']
    bars = ax.barh(labels, values, color=colors, edgecolor='white', height=0.5)
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 1000, bar.get_y() + bar.get_height()/2,
                f'{val:,}', va='center', fontsize=10)
    ax.set_title('Olympic Participation Funnel', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Athletes')
    ax.invert_yaxis()
    return fig

def pair_plot(df):
    sample = df.sample(min(1000, len(df)), random_state=42)
    pair_data = sample[['Age', 'Height', 'Weight', 'Sex']].dropna()
    pg = sns.pairplot(pair_data, hue='Sex', plot_kws={'alpha': 0.4}, height=2)
    pg.fig.suptitle('Pair Plot - Age, Height and Weight by Sex', y=1.02, fontsize=14, fontweight='bold')
    return pg.fig