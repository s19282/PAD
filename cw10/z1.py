import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

selected = option_menu(
    menu_title=None,
    options=['Questionnaire', 'Stats'],
    icons=['patch-question-fill', 'bar-chart-line-fill'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)
if selected == 'Questionnaire':
    firstname = st.text_input("First Name")
    lastname = st.text_input("Last Name")
    if st.button('Send'):
        result = 'Questionnaire saved for: {} {}'.format(firstname.title(), lastname.title())
        st.success(result)
if selected == 'Stats':
    data = st.file_uploader("Load csv", type=['csv'])
    if data is not None:
        with st.spinner("Loading..."):
            df = pd.read_csv(data)
            st.dataframe(df)
        selected_visualization = st.selectbox("Select visualisation", ("Type of clothes", "Tshirt quantity"))
        container = st.container()
        if selected_visualization == "Type of clothes":
            fig = px.histogram(df['tshirt_type'], x='tshirt_type', title="Clothes type")
            container.plotly_chart(fig, use_container_width=True)
        elif selected_visualization == "Tshirt quantity":
            fig = px.histogram(df['tshirt_quantity'], x='tshirt_quantity', title="Tshirt quantity")
            container.plotly_chart(fig, use_container_width=True)
