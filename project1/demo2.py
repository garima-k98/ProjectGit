import requests
data= {'Username':"Garima",'ID':123}
r = requests.get('https://httpbin.org/get',params=data)
print(r.text)
print(r.url)
print(r.status_code)
print(r.json())
