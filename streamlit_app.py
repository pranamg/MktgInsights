import streamlit as st
import pandas as pd
import os

st.title('🎈 Marketing Strategy Dashboard')

employees = pd.read_csv('data/employees.csv')
users = pd.read_csv('data/app_users.csv')
champions = pd.read_csv('data/champions.csv')

# Clean and preprocess data
users_df = users.dropna()
champions_df = champions.dropna()

# Aggregate KPIs
app_usage_kpis = users_df.groupby('User ID').agg({
    'Number of Visits': 'sum',
    'Duration of Stay': 'mean'
}).reset_index()

champions_kpis = champions_df.groupby('Specialization').agg({
    'Champion ID': 'count'
}).rename(columns={'Champion ID': 'Number of Champions'}).reset_index()

# Key Metrics Cards
total_employees = len(employees)
active_users = len(users_df)
total_champions = len(champions_df)
total_locations = len(set(employees['Location']))

st.subheader('Key Metrics')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Employees", total_employees)
col2.metric("Active Users", active_users)
col3.metric("Champions", total_champions)
col4.metric("Locations", total_locations)

# Tabbed Interface
tab1, tab2, tab3 = st.tabs(["Employees", "App Usage", "Champions"])

with tab1:
    st.subheader('Employees Distribution by Role')
    role_distribution = employees['Role'].value_counts().reset_index()
    role_distribution.columns = ['Role', 'Count']
    st.bar_chart(role_distribution.set_index('Role'))

    st.subheader('Average Age of Employees')
    avg_age = employees['Age'].mean()
    st.metric("Average Age", round(avg_age, 2))

with tab2:
    st.subheader('App Usage Metrics')
    st.write('App Usage KPIs')
    st.write(app_usage_kpis)

with tab3:
    st.subheader('Champions by Specialization')
    st.write('Champions KPIs by Specialization')
    st.write(champions_kpis)
