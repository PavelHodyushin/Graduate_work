import matplotlib.pyplot as plt
import pandas as pd


# Загрузка данных из CSV файла
df = pd.read_csv('russian_demography.csv', sep=',')
df.head()

# Назначение переменным данных из CSV файла
a = df['year']
b = df['population_size']
c = df['urban']
d = df['rural']


# Создание линейного графика
plt.figure(figsize=(10, 8))
plt.plot(a, b)
plt.title('Динамика численности населения РФ с 2000-2024')
plt.xlabel('Год')
plt.ylabel('Численность населения (млн.)')
plt.grid() # Отображение сетки
plt.show()


# Создание гистограммы
plt.figure(figsize=(10, 8))
plt.bar(a, c)
plt.bar(a, d)
plt.xlabel('Год')
plt.ylabel('Численность населения(млн.)')
plt.title('Численность городского и сельского населения')
plt.legend(['Городское', 'Сельское'])
plt.show()


# Построение круговой диаграммы
population1 = ['Городское', 'Сельское']
plt.figure(figsize=(10, 8))
df[df.columns[2:]].sum().plot.pie(autopct='%1.1f%%', labels=None)
plt.legend(['Городское', 'Сельское'])
plt.title('Круговая диаграмма сравнения численности городского и сельского населения')
plt.show()


