import pandas as pd

df = pd.read_csv('c:/Users/João Lucas/Cursos/Bootcamp_Python_IA/Data Science/fifa.csv')

df['Total'] = df['Overall'] + df['Potential']

print(df[['Name', 'Overall', 'Potential', 'Total']])