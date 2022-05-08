from flask import Flask, render_template, request, flash

application = Flask(__name__)

application.secret_key = "123456"
# 如果沒有設定secret_key，運行程式會出現下列錯誤
#     raise RuntimeError(
# RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.

@application.route("/hello")
def index():
    flash("What is your name?")
    return render_template("index.html")


@application.route("/greet", methods=["POST", "GET"])
def greet():
    # request.form['name_input']
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	application.run()
