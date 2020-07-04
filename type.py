import requests

response = requests.get('http://www.nagares.com/#tabs2')
string = response.content
print(type(string.decode("utf-8") ))
