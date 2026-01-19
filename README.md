This project implements a simple HTTP web service that returns the list of
publicly available GitHub gists for a given user.

The goal of this assignment is to demonstrate:
- Building a small HTTP API using a general-purpose language (Python)
- Interacting with an external REST API (GitHub Gists API)
- Writing a simple automated test
- Packaging the application using Docker with security best practices

Implementation Notes
--------------------

Running the Application Locally (Without Docker)
------------------------------------------------

Prerequisites

Python 3.10 or newer

pip installed

Step 1: Install dependencies
pip install -r requirements.txt

Step 2: Start the application
python app.py
The server will start on port 8080.

Step 3: Test the endpoint
Using curl:
curl http://localhost:8080/octocat
Or using a browser:
http://localhost:8080/octocat

Running Automated Tests
Automated tests are written using pytest.
Run tests
pytest
The test calls /octocat and validates:

HTTP status code is 200

Response format is a JSON list

Running the Application with Docker
-----------------------------------


Step 1: Build the Docker image
From the project root directory:

docker build -t github-gists-api .

Step 2: Run the container

docker run -p 8080:8080 github-gists-api
The application will now be accessible at:

http://localhost:8080/octocat
