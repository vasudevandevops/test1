from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_API = "https://api.github.com/users/{}/gists"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

@app.route("/<username>", methods=["GET"])
def get_gists(username):
    response = requests.get(
        GITHUB_API.format(username),
        headers=HEADERS,
        timeout=5
    )

    if response.status_code != 200:
        return jsonify({"error": "User not found"}), response.status_code

    gists = response.json()

    result = []
    for gist in gists:
        result.append({
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"],
            "files": list(gist["files"].keys())
        })

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
