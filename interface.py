import streamlit as st
import langchain_helper

st.title('All Time Greatest 11')
country = st.sidebar.selectbox('Countries', [
    'India', 'Australia', 'England', 'New Zealand', 'South Africa',
    'Pakistan', 'Sri Lanka', 'West Indies', 'Bangladesh', 'Afghanistan'
])


if country:
    response = langchain_helper.generate_greatest_11(country)
    st.header(response['team_name'])
    players = response['players'].split(',')
    st.write('Team')
    for p in players:
        st.write(p)