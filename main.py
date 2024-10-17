import os
from flask import Flask, request
app = Flask(__name__)

# curl -X GET "http://localhost:5000/tainted7/touch%20HELLO"
@app.route("/tainted7/<something>")
def test_sources_7(something):

    os.system(request.remote_addr)

    return "foo"

# curl -X GET "http://localhost:5000/tainted8/touch%20HELLO"
@app.route("/tainted8/<something>")
def test_sources_8(something):

    os.system(request.remote_addr)

    return "foo"

# curl -X GET "http://localhost:5000/tainted9/touch%20HELLO"
@app.route("/tainted9/<something>")
def test_sources_9(something):

    os.system(request.remote_addr)

    return "foo"

# curl -X GET "http://localhost:5000/tainted10/touch%20HELLO"
@app.route("/tainted10/<something>")
def test_sources_10(something):

    os.system(request.remote_addr)

    return "foo"

if __name__ == "__main__":
	app.run(debug=True)
