import requests
import json
BASE_URL = "https://api.bgm.tv"
"""
# 假设已经获取到的 access_token
access_token = "your_access_token"
"""
headers = {
    'User-Agent': 'iamzhz/ban-terminal (https://github.com/iamzhz/ban-terminal)',
    #'Authorization': f'Bearer {access_token}'
}
def get_api(relative_url):
    try:
        response = requests.get(BASE_URL + relative_url, headers=headers)
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        return None, str(e)  # Request Error



def check_access_token(access_token):
    url = 'https://bgm.tv/oauth/token_status'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'iamzhz/ban-terminal (https://github.com/iamzhz/ban-terminal)'
    }
    data = {
        "access_token": access_token
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return 200, response.json()
        else:
            return response.status_code, "Error"
    except requests.exceptions.RequestException as e:
        return None, e  # Request Error
    return None
def get_calendar():
    return get_api("/calendar")
def get_user_info_by_name(username):
    return get_api(f"/v0/users/{username}")
def get_search_subjects(keyword, type = 2, responseGroup = "small"):
    return get_api(f"/search/subject/{keyword}?type={type}&responseGroup={responseGroup}")