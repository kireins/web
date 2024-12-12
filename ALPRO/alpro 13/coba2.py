import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Menampilkan DataFrame statis
st.header('Data Table')
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
st.table(df)

# Menampilkan DataFrame interaktif
st.header('Interactive DataFrame')
st.dataframe(df)

# Menampilkan grafik garis
st.header('Line Chart')
line_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(line_data)

# Menampilkan grafik batang
st.header('Bar Chart')
st.bar_chart(line_data)

# Menampilkan peta
st.header('Map')
map_data = pd.DataFrame({
    'lat': [37.76, 37.76, 37.77, 37.77],
    'lon': [-122.4, -122.43, -122.42, -122.41]
})
st.map(map_data)

# Menampilkan grafik menggunakan Matplotlib
st.header('Matplotlib Chart')
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title('Matplotlib Line Chart')
st.pyplot(fig)

# Menampilkan grafik menggunakan Seaborn
st.header('Seaborn Chart')
data = sns.load_dataset('iris')
fig = sns.pairplot(data, hue='species')
st.pyplot(fig)

# Menampilkan grafik menggunakan Plotly
st.header('Plotly Chart')
df_plotly = px.data.iris()
fig_plotly = px.scatter(df_plotly, x='sepal_width', y='sepal_length', color='species')
st.plotly_chart(fig_plotly)
