import requests
from config import USER_ID, POST_ID, PROJECT_ID, TAG_ID, COMMENT_ID


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


def test_003():
    """
    GET one project
    """
    req = requests.get(f"{API_URL}/project/{POST_ID}")
    return req.status_code, req.content


def test_004():
    """
    GET one tag
    """
    req = requests.get(f"{API_URL}/tag/{TAG_ID}")
    return req.status_code, req.content


def test_005():
    """
    GET one comment
    """
    req = requests.get(f"{API_URL}/tag/{COMMENT_ID}")
    return req.status_code, req.content


def test_006():
    """
    GET version
    """
    req = requests.get(f"{API_URL}/version")
    return req.status_code, req.content


TESTS = {
    "test_001": {
        "test": test_001,
        "about": "GET one user with USER_ID. url: \"/api/user/<USER_ID>\"",
    },
    "test_002": {
        "test": test_002,
        "about": "GET one post with POST_ID. url: \"/api/post/<POST_ID>\"",
    },
    "test_003": {
        "test": test_003,
        "about": "GET one project with PROJECT_ID. url: \"/api/project/<PROJECT_ID>\"",
    },
    "test_004": {
        "test": test_004,
        "about": "GET one tag with TAG_ID. url: \"/api/tag/<TAG_ID>\"",
    },
    "test_005": {
        "test": test_005,
        "about": "GET one comment with COMMENT_ID. url: \"/api/comment/<COMMENT_ID>\"",
    },
    "test_006": {
        "test": test_005,
        "about": "GET version number. url: \"/api/version\"",
    }
}
