from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to MediCare</h1>
    <h2>Hospital Management System</h2>
    <p>Our project aims to make patient record
    management easier.</p>
    <p>More features will be added soon.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
