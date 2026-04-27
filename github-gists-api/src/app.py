import os
from flask import Flask, jsonify, request
from flask_caching import Cache
import requests

app = Flask(__name__)

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
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=30, type=int)

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
            return jsonify({"error": "User not found"}), 404
        
        response.raise_for_status()
        
        return jsonify(response.json()), 200

    except requests.exceptions.Timeout:
        return jsonify({"error": "Upstream timeout"}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Service unavailable", "details": str(e)}), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)