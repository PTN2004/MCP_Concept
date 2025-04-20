import requests

GITHUB_TOKENS = "<YOUR_GITHUB_TOKEN>"  # Replace with your actual GitHub token

#====== Check if the token is valid ======
headers = {
    "Authorization" : f"token {GITHUB_TOKENS}",   
}
url = "https://api.github.com/user/repos"
respone = requests.get(url, headers=headers)

startus = respone.status_code

if startus == 200:
    print("GITHUB TOKEN VALID")
else:
    print("GITHUB TOKEN INVALID")
