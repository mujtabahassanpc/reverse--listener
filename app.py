from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def catch():
    data = request.data.decode('utf-8')
    print(f"\n[+] Payload Data:\n{data}")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
