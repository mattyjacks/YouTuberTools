import requests

url = "https://api.elevenlabs.io/v1/voices"

response = requests.request("GET", url)

print(response.text)