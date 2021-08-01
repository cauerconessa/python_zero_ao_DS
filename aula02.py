import pandas as pd

df1 = pd.read_csv('datasets/kc_house_data.csv')

#print(df1.dtypes)

# 1. Qual a data do imóvel mais antigo no portfólio?
df1['date'] = pd.to_datetime(df1['date'])
print(df1.sort_values('date', ascending=True))

# 2. Quantos imóveis pssuem o número máximo de andares?
print(df1['floors'].unique())
print(df1[df1['floors']==3.5].shape)

# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com o preço.
df1['level'] = 'standard'
print(df1.head())

df1.loc[df1['price']>540000, 'level'] = 'high_level'
df1.loc[df1['price']<540000, 'level'] = 'low_level'
print(df1.head())

# 4. Gostaria de um relatório ordenado pelo preço
report = df1[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price', ascending=False)
print(report.head())

report.to_csv('datasets/report_aula02.csv', index=False)

#Mapa
import plotly.express as px

df1_mapa = df1[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(df1_mapa, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height= 600, margin={'r':0, 't':0, 'l':0, 'b':0})
#mapa.write_html('datasets/mapa_house_rocket.html')

