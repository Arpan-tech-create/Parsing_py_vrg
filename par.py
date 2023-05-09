import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

with open('sample.log', 'r') as file:
    data = file.readlines()

pattern = r'\[(.*?)\] \w+: (.*?)\((ip: )?(.*?)\,\sresponse code: (\d+)\)'
result = [re.search(pattern, line).groups() for line in data]

df = pd.DataFrame(result, columns=['DateTime', 'Event', 'Username', 'IP', 'Response Code'])

print(df)

sns.lineplot(data=df, y='DateTime', x='Response Code')
plt.xticks(rotation=70)
plt.show()

