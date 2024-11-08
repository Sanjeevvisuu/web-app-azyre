from flask import Flask, render_template_string
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    # Get the environment variable (with default value)
    welcome_message = os.getenv('WELCOME_MESSAGE', 'Default Welcome Message')
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Static Python App</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <h1>page -1</h1>
        <h1>{{ welcome_message }}</h1>  <!-- Use the variable from the context -->
        <p>This is a simple static Python web application served via Nginx.</p>
    </body>
    </html>
    ''', welcome_message=welcome_message)  # Pass the variable to the template

if __name__ == "__main__":
    # Run the app on host 0.0.0.0 so it's accessible inside the Docker container
    app.run(host='0.0.0.0', port=5000)
