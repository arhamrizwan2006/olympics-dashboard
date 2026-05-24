import matplotlib.pyplot as plt
import seaborn as sns

def pie_chart(df):
    fig, ax = plt.subplots(figsize=(7,7))
    medal_counts = df[df['Medal'] != 'No Medal']['Medal'].value_counts()
    if medal_counts.empty:
        ax.text(0.5, 0.5, 'No data', ha='center')
    else:
        ax.pie(medal_counts, labels=medal_counts.index, autopct='%1.1f%%',
               colors=['gold', 'silver', '#cd7f32'], startangle=90)
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