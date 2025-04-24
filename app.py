from flask import Flask, render_template
from checker import check_all_apps
import threading
import time

app = Flask(__name__)
app_status = {}

def scheduler():
    global app_status
    while True:
        app_status = check_all_apps()
        time.sleep(60)  # Check every 60 seconds

threading.Thread(target=scheduler, daemon=True).start()

@app.route("/")
def dashboard():
    return render_template("index.html", status=app_status)

if __name__ == "__main__":
    app.run(debug=True)
