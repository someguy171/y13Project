import requests
import json

# get a list of schools who use Satchel One (school_search)
# the filter specifies a certain term (can be a name, area, post code, etc.)
# in this case, KT3 5PE is used to find my school
schools = requests.get(
    # API link
    "https://api.satchelone.com/api/public/school_search?filter=kt35pe",
    # use json
    headers={"Accept": "application/smhw.v2021.5+json"},
    verify=False
).json()

# store the school ID of the first school in the list
school_id = schools["schools"][0]["id"]

# create a payload of the client ID and secret ID, to use the API
payload = {
    "client_id": "55283c8c45d97ffd88eb9f87e13f390675c75d22b4f2085f43b0d7355c1f",
    "client_secret": "c8f7d8fcd0746adc50278bc89ed6f004402acbbf4335d3cb12d6ac6497d3"
}

# create another payload containing the user's username, password, and the school ID found earlier
data = {
    "username": "sasaw004@richardchalloner.com",
    "password": "Paper900",
    "grant_type": "password",
    "school_id": school_id
}

# send these two payloads to retrieve an authentication token to access the user's data
temp = json.loads(
    requests.post(
        "https://api.satchelone.com/oauth/token",
        params=payload,
        data=data,
        headers={"Accept": "application/smhw.v2021.5+json"},
    ).text
)

# store the token
token = temp["access_token"]

# get a list of the user's to-do items (homeworks), using the token found before
response = requests.get(
    "https://api.showmyhomework.co.uk/api/todos",
    headers={
        "Accept": "application/smhw.v3+json",
        "Authorization": "Bearer" + token,
    }
).json()

# store the json response in a file
with open("apiTesting/data.json", "w") as file:
    json.dump(response, file, indent=4)