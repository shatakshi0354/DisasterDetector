from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a ChatBot instance
chatbot = ChatBot('EnvironmentalBot')

# Set up the trainer and train the chatbot using the environmental data corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.environmental_data")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chatbot.get_response(user_input).text
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
