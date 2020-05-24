from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        username = request.form.get("username")
    else:
        username = request.args.get("username")
    print(request.args)

    return 'Hello World!x'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)