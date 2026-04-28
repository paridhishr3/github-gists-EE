import os
from flask import Flask, jsonify, request, abort
from flask_caching import Cache
import requests

app = Flask(__name__)

# Configuration for Caching
config = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
cache = Cache(app)

GITHUB_API_URL = "https://api.github.com/users/{username}/gists"

@app.route('/<username>', methods=['GET'])
@cache.cached(timeout=300, query_string=True)
def get_user_gists(username):
    # 1. Validate Username: Ensure it's not just whitespace
    if not username or not username.strip() or "":
        return jsonify({"error": "Username cannot be empty"}), 400

    # 2. Validate Pagination Arguments
    # We fetch raw strings first to verify if the user provided non-numeric data
    raw_page = request.args.get('page', '1')
    raw_per_page = request.args.get('per_page', '30')

    if not raw_page.isdigit() or not raw_per_page.isdigit():
        return jsonify({"error": "page and per_page must be positive integers"}), 400

    page = int(raw_page)
    per_page = int(raw_per_page)

    params = {
        "page": page,
        "per_page": per_page
    }

    try:
        response = requests.get(
            GITHUB_API_URL.format(username=username), 
            params=params,
            timeout=10
        )
        
        if response.status_code == 404:
            return jsonify({"error": f"GitHub user '{username}' not found"}), 404
        
        response.raise_for_status()
        return jsonify(response.json()), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Upstream service error", "details": str(e)}), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)