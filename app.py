import streamlit as st

pg = st.navigation([
    st.Page('src/pages/home_page.py', title='Registro de Transações'),
    st.Page('src/pages/resume_page.py', title='Resumos Financeiros')
])

pg.run()