from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the index page
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Define a route with a variable username
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
