# Topic: Web Development with Flask
# This file demonstrates creating a basic web server using Flask

from flask import Flask  # import Flask class

app = Flask(__name__)  # create Flask app instance

# Define a route for the homepage
@app.route("/")
def home():
    return "Hello, Flask! This is your first web app."

# Run the app only if this script is executed directly
if __name__ == "__main__":
    # The server will be accessible at IP 127.0.0.1 (localhost) and port 5000
    app.run(debug=True)  # debug=True reloads server automatically



