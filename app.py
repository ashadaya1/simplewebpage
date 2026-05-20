from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Asha Today's Session</h1>
    <h2> How is the session of Azure App Service!</h2>
    """

if __name__ == '__main__':
    app.run()
