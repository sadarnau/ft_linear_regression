import pandas
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pandas.read_csv('data.csv')

figure(figsize=(20, 10), dpi=80)
plt.scatter(df['km'], df['price'])
plt.ylabel('price')
plt.xlabel('mileage (Km)')

plt.show()