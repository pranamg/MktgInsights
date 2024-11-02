import streamlit as st
from data_generation import generate_employees, generate_app_users, generate_champions

st.title('🎈 App Name')

employees = generate_employees()
users = generate_app_users(employees)
champions = generate_champions(users)

st.write('Employees')
st.write(employees)

st.write('App Users')
st.write(users)

st.write('Champions')
st.write(champions)
