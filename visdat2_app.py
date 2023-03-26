import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# membaca file csv
data = pd.read_csv('factbook.csv')

# menampilkan judul aplikasi
st.title('Visualisasi Data')

# menampilkan dataframe
st.write(data)

# membuat histogram
st.subheader('Histogram')
plt.hist(data['Area'], bins=range(min(data['Birth rate']), max(data['Death rate']) + 1, 10))
st.pyplot()

# membuat scatter plot
st.subheader('Scatter Plot')
plt.scatter(data['Area'], data['Birth rate'])
st.pyplot()
