import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
while True:
    try:
        file_path = 'udemy_courses_extended.csv'
        data = pd.read_csv(file_path)
        break
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        continue

paid_courses = data[data['is_paid'] == True]
free_courses = data[data['is_paid'] == False]

# a. Количество курсов
fig_count = go.Figure()
fig_count.add_trace(go.Bar(
    x=['Платные курсы', 'Бесплатные курсы'],
    y=[len(paid_courses), len(free_courses)],
    text=[len(paid_courses), len(free_courses)],
    textposition='auto',
    marker_color=['#3498db', '#e74c3c']
))
fig_count.update_layout(
    title='Количество платных и бесплатных курсов',
    yaxis_title='Количество курсов',
    template='plotly_white',
    height=600,
    width=800
)
fig_count.write_image('courses_count.png')
fig_count.show()

# b. Максимальное, среднее и минимальное количество подписчиков
fig_sub = make_subplots(
    rows=1, cols=3,
    subplot_titles=('Максимальное количество подписчиков', 
                    'Среднее количество подписчиков', 
                    'Минимальное количество подписчиков')
)

# Максимальное количество подписчиков
max_subscribers = [paid_courses['num_subscribers'].max(), free_courses['num_subscribers'].max()]
fig_sub.add_trace(
    go.Bar(
        x=['Платные курсы', 'Бесплатные курсы'],
        y=max_subscribers,
        text=[f'{x:,}' for x in max_subscribers],
        textposition='auto',
        marker_color=['#3498db', '#e74c3c']
    ),
    row=1, col=1
)

# Среднее количество подписчиков
avg_subscribers = [int(paid_courses['num_subscribers'].mean()), int(free_courses['num_subscribers'].mean())]
fig_sub.add_trace(
    go.Bar(
        x=['Платные курсы', 'Бесплатные курсы'],
        y=avg_subscribers,
        text=[f'{x:,}' for x in avg_subscribers],
        textposition='auto',
        marker_color=['#3498db', '#e74c3c']
    ),
    row=1, col=2
)

# Минимальное количество подписчиков
min_subscribers = [paid_courses['num_subscribers'].min(), free_courses['num_subscribers'].min()]
fig_sub.add_trace(
    go.Bar(
        x=['Платные курсы', 'Бесплатные курсы'],
        y=min_subscribers,
        text=[f'{x:,}' for x in min_subscribers],
        textposition='auto',
        marker_color=['#3498db', '#e74c3c']
    ),
    row=1, col=3
)

fig_sub.update_layout(
    title_text='Статистика по количеству подписчиков',
    height=600,
    width=1200,
    showlegend=False,
    template='plotly_white'
)
fig_sub.write_image('subscribers_stats.png')
fig_sub.show()

# c. Количество курсов для каждого уровня
levels = data['level'].unique()
paid_level_counts = [len(paid_courses[paid_courses['level'] == level]) for level in levels]
free_level_counts = [len(free_courses[free_courses['level'] == level]) for level in levels]

fig_levels = go.Figure()
fig_levels.add_trace(go.Bar(
    x=levels,
    y=paid_level_counts,
    name='Платные курсы',
    text=paid_level_counts,
    textposition='auto',
    marker_color='#3498db'
))
fig_levels.add_trace(go.Bar(
    x=levels,
    y=free_level_counts,
    name='Бесплатные курсы',
    text=free_level_counts,
    textposition='auto',
    marker_color='#e74c3c'
))

fig_levels.update_layout(
    title='Распределение курсов по уровням сложности',
    xaxis_title='Уровень сложности',
    yaxis_title='Количество курсов',
    barmode='group',
    template='plotly_white',
    height=600,
    width=1000
)
fig_levels.write_image('courses_by_level.png')
fig_levels.show()

print("Анализ завершен. Результаты сохранены в виде изображений.")
