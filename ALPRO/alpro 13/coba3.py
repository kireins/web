import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Menambahkan judul aplikasi
st.title('Task Manager App')

# Menambahkan sidebar
st.sidebar.title('Menu')
option = st.sidebar.selectbox('Select an option:', ['Insert Data', 'Search', 'Edit'])
st.sidebar.write('You selected:', option)

# Mengatur kolom
col1, col2, col3 = st.columns(3)
with col1:
    st.header('Welcome to task manager')
    st.write('This is column 1.')
    # Menampilkan grafik garis
    line_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(line_data)
with col2:
    st.header('Column 2')
    st.write('This is column 2.')
    # Menampilkan DataFrame interaktif
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
with col3:
    st.header('Column 3')
    st.write('This is column 3.')
    # Menampilkan grafik Plotly
    df_plotly = px.data.iris()
    fig_plotly = px.scatter(df_plotly, x='sepal_width', y='sepal_length', color='species')
    st.plotly_chart(fig_plotly)

# Mengatur kontainer
container = st.container()
container.header('This is a container')
container.write('Containers allow you to create sub-sections within your app.')
# Menampilkan grafik Seaborn dalam kontainer
data = sns.load_dataset('iris')
fig = sns.pairplot(data, hue='species')
container.pyplot(fig)
