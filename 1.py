import re

line = '127.0.0.1 - - [09/May/2023 18:36:32] "GET /api/v1/users HTTP/1.1" 200 -'

pattern = r'\[(.*?)\]'
timestamp = re.findall(pattern, line)[0] 

print(timestamp)
