import requests

def send_text_to_rasa(text):
    """
        Rasa message format:
        {
        "sender": "test_user",  // sender ID of the user sending the message
        "message": "Hi there!"
        }
    """
    url = "http://localhost:5005/webhooks/rest/webhook"
    obj_to_send = {
        "sender": "test_user",
        "message": text
    }
    req = requests.post(url, json=obj_to_send)
    if req.status_code == requests.codes.ok:
        print("it's okey")
    else:
        print("something is wrong")
