from Embed_text import initialize, embed
from flask import Flask, request

app = Flask(__name__)

@app.route('/embed/')
def get_res():
    # Getting Input
    text = request.args.get('text')
    # Getting Result
    result = embed(text)
    # Returning Result
    return result


@app.route('/')
def default_page():
    return '<html><body><h3>Enter Text in the following format:</h3><p><b>http://127.0.0.1:5000</b><i>/embed/?text=</i><u>your_text_here</u></p></body></html>'


if __name__ == '__main__':
    initialize()
    app.run(debug=False)
