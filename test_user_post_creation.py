import requests

base_url = 'https://gorest.co.in/public-api'
headers = {
    'Authorization': 'Bearer 243b52d0480f0fe84d23e17a8a57d6f6aac6b729794c610cca4d77eaeb359ab3',
    'Content-Type': 'application/json'
}


def create_user():
    endpoint = f'{base_url}/users'
    payload = {
        'name': 'user_n1 test_n1',
        'email': 'ut_n1@example.com',
        'gender': 'male',
        'status': 'active'
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    return response.json()


def create_post(user_id, title, body):
    endpoint = f'{base_url}/users/{user_id}/posts'
    payload = {
        'title': title,
        'body': body
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    return response.json()


def delete_user(user_id):
    endpoint = f'{base_url}/users/{user_id}'
    response = requests.delete(endpoint, headers=headers)
    return response.status_code


def test_post_creation():
    user_response = create_user()
    assert user_response['code'] == 201, f"Failed to create user: {user_response['data']}"

    user_id = user_response['data']['id']

    post_title = 'Test Post Title'
    post_body = 'This is the body of the test post.'
    post_response = create_post(user_id, post_title, post_body)
    assert post_response['code'] == 201, f"Failed to create post: {post_response['data']}"

    delete_response_code = delete_user(user_id)
    assert delete_response_code == 200, f"Failed to delete user: {delete_response_code}"


test_post_creation()
