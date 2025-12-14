import requests

TOKEN = "7qo1ymgxjwuf2jt6"
ADMIN_NUMBER = "923132272190"

def send_whatsapp(message, number):
    url = "https://api.ultramsg.com/instance156001/messages/chat"
    payload = {
        "token": TOKEN,
        "to": number,
        "body": message
    }
    response = requests.post(url, data=payload)
    return response.status_code



# import requests

# # 🔐 UltraMsg Details
# TOKEN = "7qo1ymgxjwuf2jt6"
# ADMIN_NUMBER = "923132272190"

# def send_whatsapp(message, number):
#     # ✅ Full URL from UltraMsg dashboard
#     url = "https://api.ultramsg.com/instance156001/messages/chat"

#     payload = {
#         "token": TOKEN,
#         "to": number,
#         "body": message
#     }

#     response = requests.post(url, data=payload)
#     return response.status_code



# import requests

# INSTANCE_ID = "instance156001"
# TOKEN = "7qo1ymgxjwuf2jt6"
# ADMIN_NUMBER = "923132272190"

# def send_whatsapp(message, number):
#     url = f"https://api.ultramsg.com/instance156001/"
#     payload = {
#         "token": TOKEN,
#         "to": number,
#         "body": message
#     }
#     requests.post(url, data=payload)
