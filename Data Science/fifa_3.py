import pandas as pd


df = pd.read_csv('c:/Users/João Lucas/Cursos/Bootcamp_Python_IA/Data Science/fifa.csv')

dados = df['Total'] = df['Overall'] + df['Potential']

dados.to_csv('fifa_novo.csv', index=False, sep='\t')