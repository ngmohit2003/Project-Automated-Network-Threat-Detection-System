# dashboard/app.py

from flask import Flask, render_template
from collections import defaultdict

app = Flask(__name__)

LOG_PATH = "../threats.log"

@app.route("/")
def index():
    threat_counts = defaultdict(int)
    ip_counts = defaultdict(int)

    try:
        with open(LOG_PATH, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 3:
                    threat = parts[1].strip()
                    ip = parts[2].replace("Source IP:", "").strip()
                    threat_counts[threat] += 1
                    ip_counts[ip] += 1
    except FileNotFoundError:
        pass

    total_threats = sum(threat_counts.values())

    return render_template("index.html", 
                           threat_counts=dict(threat_counts),
                           ip_counts=dict(ip_counts),
                           total_threats=total_threats)

if __name__ == "__main__":
    app.run(debug=True)
