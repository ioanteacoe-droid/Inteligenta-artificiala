import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
print(df.head())

df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
print(df.head())


top_students = df[(df['test preparation course'] == 'completed') & (df['average_score'] > 80)]
print(top_students.head())


parental_impact = df.groupby('parental level of education')['average_score'].mean().sort_values(ascending=False)
print(parental_impact)

import pandas as pd

# Încărcăm fișierul
df = pd.read_csv('StudentsPerformance.csv')

# Definirea condițiilor pentru filtrare
studii_superioare = ["master's degree", "bachelor's degree"]

rezultat_filtrare = df[
    (df['gender'] == 'female') &
    (df['parental level of education'].isin(studii_superioare)) &
    (df['math score'] >= 85) &
    (df['math score'] <= 95)
]

print("Elevele care îndeplinesc criteriile:")
print(rezultat_filtrare)

import pandas as pd


df = pd.read_csv('StudentsPerformance.csv')

print("--- Tipuri de variabile ---")
print(df.dtypes)


filtre_cerinta_1 = (df['gender'] == 'female') & \
                   (df['parental level of education'].isin(["master's degree", "bachelor's degree"])) & \
                   (df['math score'] >= 85) & (df['math score'] <= 95)

rezultat_eleve = df[filtre_cerinta_1]


df['Total Score'] = df['math score'] + df['reading score'] + df['writing score']
top_10 = df.sort_values(by='Total Score', ascending=False).head(10)


print("\n--- Rezultat Filtrare Eleve ---")
print(rezultat_eleve)

print("\n--- Top 10 Elevi după Scor Total ---")
print(top_10)