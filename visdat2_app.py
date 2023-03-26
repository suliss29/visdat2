import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


with st.expander("Eksplorasi Data"):
    st.snow()
    st.title('Configure Plot')
    st.header('Pilih data')
    option_x = st.selectbox(
        '',
        (' gdppercap ', '  Area ', ' birthrate ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' Country ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' lifeexpectatbirth ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' population ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
    st.write('X :', option_x)

    option_y = st.selectbox(
        '',
        (' lifeexpectatbirth ', '  Area ', ' birthrate ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' gdppercap ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' Country ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' population ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
    st.write('Y :', option_y)

    option_size = st.selectbox(
        '',
        (' population ', '  Area ', ' birthrate ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' gdppercap ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' lifeexpectatbirth ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' Country ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
    st.write('Size :', option_size)

    option_color = st.selectbox(
        '',
        (' birthrate ', '  Area ', ' Country ', '   Current account balance  ', '  Death rate ', '  Electricity consumption ', '   Electricity production  ', '   Exports  ', '   GDP  ', ' gdppercap ', '  GDP real growth rate ', '   Highways  ', '   Imports  ', '  Industrial production growth rate ', '  Infant mortality rate ', '  Inflation rate  ', '   Internet users  ', '  Investment ', '   Labor force  ', ' lifeexpectatbirth ', '  Military expenditures ', '   Natural gas consumption  ', '   Oil consumption  ', ' population ', '  Public debt ', '  Railways ', '   Reserves of foreign exchange & gold  ', '  Total fertility rate ', '  Unemployment rate '))
    st.write('Color :', option_color)

bub = st.slider('Ukuran Bubble', 1, 100, 60)
df = pd.read_csv('factbook.csv')
fig1 = px.scatter(df,
    x=option_x,
    y=option_y,
    size=option_size,
    color=option_color,
    size_max=bub,
    hover_data=[option_size],
   color_continuous_scale=px.colors.sequential.Viridis,
)
st.plotly_chart(fig1)
