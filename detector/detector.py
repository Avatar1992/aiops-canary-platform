import requests
import statistics
import os

LOKI_URL = os.getenv("LOKI_URL", "http://loki:3100")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPO")  # avatar1992/aiops-canary-platform

def query_error_rate():
    query = 'count_over_time({job="app"} |= "ERROR" [1m])'
    r = requests.get(
        f"{LOKI_URL}/loki/api/v1/query",
        params={"query": query}
    )
    data = r.json()["data"]["result"]
    return len(data)

def create_github_issue(count):
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    payload = {
        "title": "🚨 Anomaly Detected: ERROR spike",
        "body": f"Detected abnormal ERROR rate.\n\nCount: {count}"
    }
    requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
    error_count = query_error_rate()

    # simple anomaly rule
    if error_count > 5:
        create_github_issue(error_count)
        print("Anomaly detected. GitHub issue created.")
    else:
        print("System normal.")

