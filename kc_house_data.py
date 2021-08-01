import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

#1- Quantas casas estão disponíveis para compra?
print(data.shape[0])

#2. Quantos atributos as casas possuem?
print(data.shape[1])

#3. Quais são os atributos das casas?
print(data.columns)

#4. Qual a casa mais cara ( casa com o maior valor de venda )?
print(data[['id', 'price']].sort_values('price', ascending=False))

#5. Qual a casa com o maior número de quartos?
print(data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False))

#6. Qual a soma total de quartos do conjunto de dados?
print(data['bedrooms'].sum())

#7. Quantas casas possuem 2 banheiros?
print(data[data['bathrooms']==2].shape)

#8. Qual o preço médio de todas as casas no conjunto de dados?
print(data['price'].mean())

#9. Qual o preço médio de casas com 2 banheiros?
print(data.loc[data['bathrooms']==2, 'price'].mean())

#10. Qual o preço mínimo entre as casas com 3 quartos?
print(data.loc[data['bedrooms']==3, 'price'].min())

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
#OBS: 1 pé quadrado = 0,09 metros quadrados
data['m2_living'] = data['sqft_living']*0.092
print(data[data['m2_living']>300].shape)

#12. Quantas casas tem mais de 2 andares?
print(data[data['floors']>2].shape)

#13. Quantas casas tem vista para o mar?
print(data[data['waterfront']==1].shape)

#14. Das casas com vista para o mar, quantas tem 3 quartos?
print(data[(data['waterfront']==1)&(data['bedrooms']==3)].shape)

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
print(data[(data['m2_living']>300)&(data['bathrooms']>2)].shape)
