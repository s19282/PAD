import streamlit as sl
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly.express as px

selected = option_menu(
    menu_title=None,
    options=['Questionnaire', 'Stats'],
    icons=['patch-question-fill', 'bar-chart-line-fill'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

if selected == 'Stats':
    data = sl.file_uploader("Load csv", type=['csv'])
    if data is not None:
        with sl.spinner("Loading..."):
            df = pd.read_csv(data)
            sl.dataframe(df)
        selected_visualization = sl.selectbox("Select visualisation", ("Type of clothes", "Gender of client"))
        container = sl.container()
        if selected_visualization == "Type of clothes":
            fig = px.histogram(df['tshirt_type'], x='tshirt_type', title="Clothes type")
            container.plotly_chart(fig, use_container_width=True)
        elif selected_visualization == "Gender of client":
            fig = px.histogram(df['gender'], x='gender', title="Client's gender")
            container.plotly_chart(fig, use_container_width=True)
if selected == 'Questionnaire':
    firstname = sl.text_input("First Name")
    lastname = sl.text_input("Last Name")
    if sl.button('Send'):
        result = 'Questionnaire saved for: {} {}'.format(firstname.title(), lastname.title())
        sl.success(result)
