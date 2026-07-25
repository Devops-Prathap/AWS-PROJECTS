from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>AWS CI/CD Project</h1>
    <h2>Deployment Successful!</h2>

    <p>Services Used:</p>
    <ul>
        <li>GitHub</li>
        <li>AWS CodePipeline</li>
        <li>AWS CodeBuild</li>
        <li>AWS CodeDeploy</li>
        <li>Docker Hub</li>
        <li>Amazon EC2</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
