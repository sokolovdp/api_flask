from collections import defaultdict

MAX_REQUESTS_PER_USER = 5
user_requests_counter = defaultdict(int)


def max_user_requests(username: str) -> bool:
    user_requests_counter[username] += 1
    return not user_requests_counter[username] < MAX_REQUESTS_PER_USER


def reset_user_counter(username: str):
    user_requests_counter[username] = 0


def max_requests_message() -> dict:
    return {"exceeded limit of requests per user session": MAX_REQUESTS_PER_USER}
