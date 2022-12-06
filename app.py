from flask import Flask, render_template, jsonify, request
import process


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/get")
def get_bot_response():
    userText = str(request.args.get('msg'))
    return process.generate_response(userText)


if __name__ == "__main__":
    app.run()

# @app.route('/', methods=["GET", "POST"])
# def index():
#     return render_template('index.html', **locals())

# @app.route('/bot', methods=["GET", "POST"])
# def bot():
#     return render_template('chatbot.html', **locals())



# @app.route('/chatbot', methods=["GET", "POST"])
# def chatbotResponse():

#     if request.method == 'POST':
#         the_question = request.form['question']

#         response = processor.chatbot_response(the_question)

#     return jsonify({"response": response })



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='8888', debug=True)
