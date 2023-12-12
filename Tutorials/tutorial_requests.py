import requests

response = requests.get("https://api.github.com")
#print(response.status_code) # 200 means succesful, 404 means not found
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")

# requests simplifies if statements
if response:
    print("Success!")
else:
    print("An error has occurred.")

#print(response.content) # get the response in bytes
#print(response.text) # decode the response into string with utf-8
#print(response.json()) # get dictionary like json.loads()
#print(response.headers) # headers to get useful information
print(response.headers["Content-Type"]) # access header dictionary
