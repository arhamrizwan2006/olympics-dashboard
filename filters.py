import pandas as pd
import os

def load_data():
    if os.path.exists('athlete_events.csv'):
        athletes = pd.read_csv('athlete_events.csv')
        regions = pd.read_csv('noc_regions.csv')
    elif os.path.exists('data/athlete_events.csv'):
        athletes = pd.read_csv('data/athlete_events.csv')
        regions = pd.read_csv('data/noc_regions.csv')
    else:
        athletes = pd.read_csv('https://raw.githubusercontent.com/arhamrizwan2006/olympics-dashboard/main/athlete_events.csv')
        regions = pd.read_csv('https://raw.githubusercontent.com/arhamrizwan2006/olympics-dashboard/main/noc_regions.csv')

    df = athletes.merge(regions, on='NOC', how='left')
    df['Medal'] = df['Medal'].fillna('No Medal')
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Height'] = df['Height'].fillna(df['Height'].median())
    df['Weight'] = df['Weight'].fillna(df['Weight'].median())
    df['region'] = df['region'].fillna(df['Team'])
    df = df.drop(columns=['notes'], errors='ignore')
    return df

def apply_filters(df, season, year_range, sex, sports, search):
    if season != 'All':
        df = df[df['Season'] == season]
    df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    if sex != 'All':
        df = df[df['Sex'] == sex]
    if sports:
        df = df[df['Sport'].isin(sports)]
    if search:
        df = df[df['Name'].str.contains(search, case=False, na=False)]
    return df