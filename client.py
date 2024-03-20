import requests

while True:
    message = input("Enter a message (or 'q' to quit): ")
    if message.lower() == 'q':
        break

    url = 'http://localhost:5000/send_message'
    data = {'message': message}
    response = requests.post(url, data=data)

    print(response.text)