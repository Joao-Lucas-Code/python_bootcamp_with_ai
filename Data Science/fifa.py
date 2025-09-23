import pandas as pd

df = pd.read_csv('c:/Users/João Lucas/Cursos/Bootcamp_Python_IA/Data Science/fifa.csv')

# print(df.iloc[2,2])

noventa_mais = df.loc[df['Overall'] > 90, ['Name', 'Overall', 'Club']]  # Jogadores com overall maior que 90

print(noventa_mais)