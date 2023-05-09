import base64
import requests

# set up variables with your client ID and secret
client_id = "961d9cfe0e7c426da68d7932c2693fc9"
client_secret = "9f329e3768eb4681aab10caf2de7f10b"

# concatenate the client ID and secret with a colon and base64-encode the result
client_credentials = f"{client_id}:{client_secret}"
client_credentials_b64 = base64.b64encode(client_credentials.encode()).decode()

# set up headers and payload for the request
headers = {
    "Authorization": f"Basic {client_credentials_b64}"
}
data = {
    "grant_type": "client_credentials"
}

# make a POST request to the Spotify Accounts service to get an access token
response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

# extract the access token from the response JSON
access_token = response.json()["access_token"]

print(access_token)