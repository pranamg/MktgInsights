import streamlit as st
import pandas as pd
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

st.write('Employees')
st.write(employees)

st.write('App Users')
st.write(users_df)

st.write('Champions')
st.write(champions_df)

st.write('App Usage KPIs')
st.write(app_usage_kpis)

st.write('Champions KPIs by Specialization')
st.write(champions_kpis)
