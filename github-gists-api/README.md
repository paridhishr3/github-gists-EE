# README for GitHub Gists API

## Overview
This project is a simple HTTP web server API that interacts with the GitHub API to fetch and return a list of publicly available Gists for a specified user. It is built using Flask and is containerized using Docker.

## Features
- Fetch user Gists from the GitHub API
- Automated tests to ensure functionality
- Docker containerization for easy deployment

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Docker (for containerization)

### Installation
1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd github-gists-api
   ```

2. Install the required dependencies:
   ```
   python3 -m venv .venv
   pip3 install -r requirements.txt
   ```

### Running the Application
To run the application locally, execute the following command:
```
python3 src/app.py
```
The server will start and listen for requests on `http://localhost:8080`.

### Using Docker
To build and run the application in a Docker container, use the following commands:
```
docker build -t github-gists-api .
docker run -p 8080:8080 github-gists-api
```

### API Endpoint
- **GET /<USER>**: Returns a list of publicly available Gists for the specified GitHub user.

### Running Tests
To run the automated tests, execute:
```
pytest tests/

or 

python3 -m pytest

```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.