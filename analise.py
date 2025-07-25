import pandas as pd
import matplotlib.pyplot as plt

# Carregue o arquivo CSV (use o caminho correto no seu PC)
df = pd.read_csv('test_groupby_data.csv')

# Agrupar os dados por data e contar usuários únicos
daily_users = df.groupby('date')['user_id'].nunique()

# Plotar gráfico de linha
daily_users.plot(kind='line')

# Adicionar título e rótulo do eixo Y
plt.title('Daily users')
plt.ylabel('Number of users')

# Rotacionar os rótulos do eixo X
plt.xticks(rotation=45)

# Mostrar o gráfico
plt.show()
