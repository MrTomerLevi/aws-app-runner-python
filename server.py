from flask import Flask
import os

PORT = os.environ['PORT']
name = 'simple-server'
MESSAGE = "Malabi makabi stopkes!"
print("Message: '" + MESSAGE + "'")

app = Flask(__name__)


@app.route("/")
def root():
  print("Handling web request. Returning message.")
  result = MESSAGE.encode("utf-8")
  return result


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)