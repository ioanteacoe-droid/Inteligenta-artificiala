import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print("Primele randuri din setul de date ")
print(df.head())
# 2.
print(" Jucatori peste 40 de ani")
peste_40 = df[df['Age'] > 40]
print(peste_40.head(10))

# 3.
print(" Jucatori buni si tineri ")
print(df[(df['Overall'] >= 85) & (df['Age'] < 25)])

# 4.
print(" Sortare dupa Skill Moves ")
print(df.sort_values(by='Skill Moves', ascending=False).head())

#5.
print(" Contracte care expira in 2021 ")
# Curatam coloana de ani in caz ca sunt probleme
df['Contract Valid Until'] = pd.to_numeric(df['Contract Valid Until'], errors='coerce')
print(df[df['Contract Valid Until'] <= 2021].head())

# 6.
print(" Statistici set de date ")
print(f"Randuri: {df.shape[0]} | Coloane: {df.shape[1]}")
print(f"Jucatori unici: {df['ID'].nunique()}")

#7.
top_5_tari = df['Nationality'].value_counts().head(5)
print(top_5_tari)
# 8
top_5_tari.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Proportia jucatorilor pe nationalitati (Top 5)')
plt.ylabel('') # Scoatem eticheta de pe verticala pentru aspect
plt.show()
#9.
print("  Media vitezei pe nationalitati (primele 5)")
# Folosim groupby pentru a grupa jucatorii din aceeasi tara
media_viteza = df.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()
print(media_viteza.head(5))
