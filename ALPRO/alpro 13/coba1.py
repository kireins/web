import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Judul aplikasi
st.title('Streamlit Demo App')

# Header dan subheader
st.header('Introduction')
st.subheader('This app demonstrates various Streamlit features')

# Teks dan Markdown
st.text('This is some simple text.')
st.markdown('**This is bold text** and _this is italic text_. You can also use [markdown links](<https://www.streamlit.io>).')

# Input teks
name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello, {name}!')

# Input angka
age = st.number_input('Enter your age:', min_value=0, max_value=120, value=25)
st.write(f'Your age is {age}.')

# Selectbox
favorite_color = st.selectbox('Select your favorite color:', ['Red', 'Green', 'Blue'])
st.write(f'Your favorite color is {favorite_color}.')

# Multiselect
hobbies = st.multiselect('Select your hobbies:', ['Reading', 'Traveling', 'Cooking', 'Gaming'])
st.write('Your hobbies are:', ', '.join(hobbies))

# Menampilkan gambar
st.image(
            "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )
# Menampilkan audio
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

# Menampilkan video
st.video('https://www.youtube.com/watch?v=3jZ5vnv-LZc')

# Menampilkan data dalam tabel dan DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
st.table(df)
st.dataframe(df)

# Menampilkan grafik matplotlib
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title('Matplotlib Line Chart')
st.pyplot(fig)

# Menampilkan grafik Plotly
df_plotly = px.data.iris()
fig_plotly = px.scatter(df_plotly, x='sepal_width', y='sepal_length', color='species')
st.plotly_chart(fig_plotly)

# Menampilkan LaTeX
st.latex(r'''
a + ar + ar^2 + ar^3 + \\cdots + ar^n
''')

# Tombol klik
if st.button('Click me'):
    st.write('Button clicked!')

# Layout dengan kolom
col1, col2 = st.columns(2)
with col1:
    st.write('This is column 1')
with col2:
    st.write('This is column 2')

# Sidebar
st.sidebar.title('Sidebar Title')
st.sidebar.selectbox('Select option:', ['Option A', 'Option B'])
