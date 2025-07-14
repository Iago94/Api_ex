import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"
data = {
    "pessoa":
    {"nome":"Iago", 
    "professor":"Analista"}

}
params =  {
    "dataIni":"2025-01-01",
    "dataFim":"2025-12-31"
}

# response = requests.get(url)
response = requests.post(url, json=data, params=params)

print (response.request.url)
print(response.text)

# https://httpbin.org/post?dataIni=2025-01-01&dataFim=2025-12-31&teste=