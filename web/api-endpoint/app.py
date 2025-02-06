from flask import Flask, request, jsonify, render_template
import base64

token = "YOU_@re_G3TtInG_c1o$ER"
flag = "flag{yOU_Ma$t3r3d_enum3R47I0n}"

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html") 
@app.route('/api')
def api():
    # return "You think I will expose my API Endpoints? No way!"
    return render_template("api.html")

@app.route('/api/access')
def access():
    # Encode the token in base64 and return it
    return jsonify({'admin-token': base64.b64encode(token.encode()).decode('utf-8')})

@app.route('/api/flag')
def reveal_flag():

    # Get the token provided by the user
    user_token = request.args.get("token")
    if not user_token:
        return render_template("flag.html", message="Token parameter required")
    if user_token == token:
        return render_template("flag.html", message=f"Here is go: {flag}")
    else:
        return render_template("flag.html", message="Flag Access Forbidden")
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
