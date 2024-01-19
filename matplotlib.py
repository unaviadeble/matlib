import matplotlib.pyplot as plt
import pandas as pd
# Загрузка данных из файла в Pandas DataFrame (замените 'your_dataset.csv' на свой файл)
df = pd.read_csv('random_data.csv')

# Пример: построение графика зависимости двух столбцов
plt.plot(df['Name'], df['Age'], label='Линия данных')

# Добавление заголовка и подписей к осям
plt.title('Пример графика из датасета')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
# Отображение графика
plt.show()