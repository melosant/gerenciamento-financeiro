import streamlit as st

pg = st.navigation([
    st.Page('src/pages/home_page.py', title='Registro de Transações'),
    st.Page('src/pages/registers_show.py', title='Seus Registros'),
    st.Page('src/pages/deep_resume.py', title='Resumos Financeiros')
])

pg.run()