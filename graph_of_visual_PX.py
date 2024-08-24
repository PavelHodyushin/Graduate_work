import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


# Загрузка данных из CSV файла
df = pd.read_csv('russian_demography.csv', sep=',')
df.head()

a = df['year']
b = df['population_size']
c = df['urban']
d = df['rural']


# Создание диаграммы
fig = px.bar(df, x="year",
             y="population_size",
             title= "Динамика численности населения РФ с 2000-2024",
             template="simple_white")
fig.update_layout(yaxis_title='Численность(млн)',
                  xaxis_title='Год',
                  title={'font': dict(size=25), 'x': 0.5})
fig.update_traces(hovertemplate='Численность(млн): %{y} <br> Год: %{x}')
fig.show()


# Создание двойного линейного графика
fig = go.Figure()
fig.add_trace(go.Scatter(x=a, y=c, mode='lines+markers', name='Городское'))
fig.add_trace(go.Scatter(x=a, y=d, mode='lines+markers', name='Сельское'))
fig.update_layout(title='Сравнение городского и сельского населения')
fig.update_layout(yaxis_title='Численность(млн)',
                   xaxis_title='Год',
                   title={'font': dict(size=25), 'x': 0.5},
                   legend_orientation="h")
fig.update_traces(hoverinfo="all", hovertemplate="Год: %{x}<br>Численность: %{y}")
fig.show()


# Создание круговой диаграммы
vals = [df['urban'].sum(), df['rural'].sum()]
labels = ['Городское', 'Сельское']

fig = px.pie(df,  values=vals, names=labels,
                  title="Круговая диаграмма сравнения численности городского и сельского населения")
fig.update_layout(title={'font': dict(size=15), 'x': 0.5})
fig.show()
