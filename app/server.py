from flask import Flask
import os

PORT = name = os.environ['PORT']
NAME = os.environ['NAME']

app = Flask(NAME)


@app.route("/")
def root():
    print("Handling web request. Returning message.")
    result = "Malbi Malabi Stopkes".encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
