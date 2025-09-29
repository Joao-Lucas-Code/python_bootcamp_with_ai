import pandas as pd
df = pd.read_csv('c:/Users/João Lucas/Cursos/Bootcamp_Python_IA/Data Science/pokemon.csv')

filter1 = df['generation'] == 1

filter2 = df['type1'] == 'Grass'
filter3 = df['type2'] == 'Poison'


print(df[filter2 & filter3])