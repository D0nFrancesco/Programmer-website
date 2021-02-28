import requests
from config import USER_ID, POST_ID


API_URL = 'http://localhost:8000/api'


def test_001():
    """
    GET one user
    """
    req = requests.get(f"{API_URL}/user/{USER_ID}")
    return req.status_code, req.content


def test_002():
    """
    GET one post
    """
    req = requests.get(f"{API_URL}/post/{POST_ID}")
    return req.status_code, req.content
