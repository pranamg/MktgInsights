import streamlit as st
import pandas as pd
import os
from data_generation import generate_employees, generate_app_users, generate_champions, clean_and_preprocess_data, aggregate_kpis

st.title('🎈 Marketing Strategy Dashboard')

employees = generate_employees()
users = generate_app_users(employees)
champions = generate_champions(users)

# Clean and preprocess data
users_df = clean_and_preprocess_data(pd.DataFrame(users))
champions_df = clean_and_preprocess_data(pd.DataFrame(champions))

# Aggregate KPIs
app_usage_kpis, champions_kpis = aggregate_kpis(users_df, champions_df)

# Key Metrics Cards
total_employees = len(employees)
active_users = len(users_df)
total_champions = len(champions_df)
total_locations = len(set([employee['Location'] for employee in employees]))

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
    role_distribution = pd.DataFrame(employees)['Role'].value_counts().reset_index()
    role_distribution.columns = ['Role', 'Count']
    st.bar_chart(role_distribution.set_index('Role'))

    st.subheader('Average Age of Employees')
    avg_age = pd.DataFrame(employees)['Age'].mean()
    st.metric("Average Age", round(avg_age, 2))

with tab2:
    st.subheader('App Usage Metrics')
    st.write('App Usage KPIs')
    st.write(app_usage_kpis)

with tab3:
    st.subheader('Champions by Specialization')
    st.write('Champions KPIs by Specialization')
    st.write(champions_kpis)
