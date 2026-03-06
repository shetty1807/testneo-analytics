import streamlit as st

st.title("LLM Cost Dashboard")

st.write("Welcome to the LLM Cost Monitoring Dashboard")

cost = st.number_input("Enter API Cost")

if cost:
    st.write("Total Cost:", cost)