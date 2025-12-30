from flask import Flask
import logging
import time
import random
import os

app = Flask(__name__)

LOG_DIR = "/var/log/app"
LOG_FILE = f"{LOG_DIR}/app.log"

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    user_id = random.randint(1, 100)
    logging.info(f"Order processed successfully for user {user_id}")
    return "App v1: Stable version\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

