from flask import Flask, request

app = Flask(__name__)

messages = []


@app.post('/message')
def add_message():  # put application's code here
    new_message = request.json['message']
    messages.append(new_message)
    return {'message': new_message}


@app.get('/message')
def get_message():
    if len(messages) == 0:
        return {'message': ''}
    else:
        return {'message': messages.pop()}


if __name__ == '__main__':
    app.run()
