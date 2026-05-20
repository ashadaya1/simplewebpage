from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Azure App Service</h1>
    <h2> Website Deployment by Asha Successful!</h2>
    """

if __name__ == '__main__':
    app.run()