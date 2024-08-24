import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



# Загрузка данных из CSV файла
df = pd.read_csv('russian_demography.csv', sep=',')
df.head()


# Создание линейного графика
plt.figure(figsize=(14, 8))
sns.set_style("darkgrid")
sb = sns.lineplot(data=df, x="year", y="rural")
sb1 = sns.lineplot(data=df, x="year", y="urban")
plt.xlabel('Год')
plt.ylabel('Численность населения(млн.)')
plt.legend(['Сельское', '', 'Городское'])
sb.set_title("Линейные графики динамики численности сельского и городского населения ")
plt.show()


# Создание диаграммы рассеяния
plt.figure(figsize=(14, 8))
sb = sns.scatterplot(data=df, x='year', y='population_size')
sb.set_title("Диаграмма рассеяния динамики численности населения РФ с 2000-2024")
plt.show()


# Создание гистограммы
plt.figure(figsize=(14, 8))
sb = sns.barplot(x="year", y="rural", data=df, color='blue')
sb.set_title("Гистограмма численности сельского населения")
plt.show()
