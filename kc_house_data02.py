import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

data['date'] = pd.to_datetime(data['date'])
#print(data.dtypes)

# 1.Crie uma nova coluna chamada: “house_age”
# a.Se o valor da coluna “date” for maior que 2014-01-01 -> ‘new_house’
# b.Se o valor da coluna “date” for menor que 2014-01-01 -> ‘old_house’
data['house_age'] = 'house_age'
data.loc[data['date']> '2014-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age'] = 'old_house'
print(data.head())

# 2.Crie uma nova coluna chamada: “dormitory_type”
# a.Se o valor da coluna “bedrooms” for igual a 1 -> ‘studio’
# b.Se o valor da coluna “bedrooms” for igual a 2 -> ‘apartment’
# c.Se o valor da coluna “bedrooms” for maior que 2 -> ‘house’
data['dormitory_type'] = 'dormitory_type'

data.loc[data['bedrooms']==1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms']==2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms']>2, 'dormitory_type'] = 'house'
print(data.head())

# 3.Crie uma nova coluna chamada: “condition_type”
# a.Se o valor da coluna “condition” for menor ou igual a 2 -> ‘bad’
# b.Se o valor da coluna “condition” for igual a 3 ou 4 -> ‘regular’
# c.Se o valor da coluna “condition” for igual a 5 -> ‘good’
data['condition_type'] = 'condition_type'

data.loc[data['condition']<=2, 'condition_type'] = 'bad'
data.loc[data['condition']==3, 'condition_type'] = 'regular'
data.loc[data['condition']==4, 'condition_type'] = 'regular'
data.loc[data['condition']==5, 'condition_type'] = 'good'
print(data.head())

#4.	Modifique o TIPO da coluna “condition” para STRING
data['condition'] = data['condition'].astype(str)
#print(data.dtypes)

#5.	Delete as colunas: “sqft_living15” e “sqft_lot15”
print(data.columns)
data = data.drop( ['sqft_living15', 'sqft_lot15'], axis=1)
print(data.columns)

#6.	Modifique o TIPO da coluna “yr_build” para DATE
data['yr_built'] = pd.to_datetime(data['yr_built'])
print(data.dtypes)

#7.	Modifique o TIPO da coluna “yr_renovated” para DATE
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])
print(data.dtypes)

#8.	Qual a data mais antiga de construção de um imóvel?
print(data['yr_built'].unique())
print(data.sort_values('yr_built', ascending=True))
print(data['yr_built'])

#9.	Qual a data mais antiga de renovação de um imóvel?
print(data['yr_renovated'].unique())
print(data.sort_values('yr_renovated', ascending=True))
print(data['yr_renovated'])

#10.Quantos imóveis tem 2 andares?
print(data[data['floors']==2].shape)

#11.Quantos imóveis estão com a condição igual a “regular”?
print(data[data['condition_type']=='regular'].shape)

#12.Quantos imóveis estão com a condição igual a “bad” e possuem “vista para água”?
print(data[(data['condition_type']=='bad')&(data['waterfront']==3)].shape)

#13.Quantos imóveis estão com a condição igual a “good” e são “new_house”?
print(data[(data['condition_type']=='good')&(data['house_age']=='new_house')].shape)

#14.Qual o valor do imóvel mais caro do tipo “studio”?
print(data.loc[data['dormitory_type']=='studio', 'price'].max())

#15.Quantos imóveis do tipo “apartment” foram reformados em 2015?
print(data[(data['dormitory_type']=='apartment')&(data['yr_renovated']=='2015')].shape)

#16.Qual o maior número de quartos que um imóvel do tipo “house” possui?
print(data.loc[data['dormitory_type']=='house', 'bedrooms'].max())

#17.Quantos imóveis “new_house” foram reformados no ano de 2014?
print(data[(data['house_age']=='new_house')&(data['yr_renovated']=='2014-01-01')].shape)

# 18.Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo método:
# a.Direto pelo nome das colunas
# b.Pelos índices
# c.Pelos índices das linhas e o nome das colunas
# d.Índices Booleanos
print(data[['id', 'date', 'price', 'floors', 'zipcode']])
print(data.iloc[0:10, 0:17])
print(data.loc[0:10, ['id', 'date', 'price', 'floors', 'zipcode']])
print(data.loc[0:10, [True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]])

#19.Salve um arquivo .csv com somente as colunas do item 10 ao 17
report = data[['floors', 'condition_type', 'waterfront', 'dormitory_type', 'yr_renovated', 'bedrooms', 'house_age']]
print(report.head(10))

#report.to_csv('datasets/report_house_rocket.csv', index=False)

#20.	Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”
import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['darkgreen'], zoom=3, height=300)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height= 600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.write_html('datasets/mapa_house_rocket.html')
