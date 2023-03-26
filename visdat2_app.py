import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

# Load data, define hover text and bubble size
df = pd.read_excel('factbook.csv')
#df.head()

hover_text = []
bubble_size = []

for index, row in df.iterrows():
    hover_text.append(('Country : {country}<br>'+
                      'Continent : {continent}<br>'+
                      'Life expectancy at birth: {lifeExp}<br>'+
                      '  GDP per capita  : {gdp}<br>'+
                      '  Population 	: {pop}').format(country=row['Country'],
                                            continent=row['Continent'],
                                            lifeExp=row['Life expectancy at birth'],
                                            gdp=row['  GDP per capita '],
                                            pop=row['  Population ']))
    bubble_size.append(math.sqrt(row['  Population ']))

df['text'] = hover_text
df['size'] = bubble_size
sizeref = 2.*max(df['size'])/(7000)

# Dictionary with dataframes for each continent
continent_names = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']
continent_data = {continent:df.query("Continent == '%s'" %continent)
                              for continent in continent_names}

# Create figure
fig = go.Figure()

for continent_name, continent in continent_data.items():
    fig.add_trace(go.Scatter(
        x=continent['  GDP per capita '], y=continent['Life expectancy at birth'],
        name=continent_name, text=continent['text'],
        marker_size=continent['size'],
        ))

# Tune marker appearance and layout
fig.update_traces(mode='markers', marker=dict(sizemode='area',
                                              sizeref=sizeref, line_width=2))

fig.update_layout(
    title='Life Expectancy vs GDP per Capita',
    xaxis=dict(
        title='GDP per capita',
        gridcolor='white',
        type='log',
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy',
        gridcolor='white',
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)
st.plotly_chart(fig)
