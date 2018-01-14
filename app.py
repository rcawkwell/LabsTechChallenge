from flask import Flask, render_template

app = Flask(__name__)

@app.route('/rgc2137', methods=['GET'])
def mypage():
    return render_template('rgc2137.html')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
