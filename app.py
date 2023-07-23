from flask import Flask
import sys

app = Flask(__name__)
# cors = CORS(app)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
