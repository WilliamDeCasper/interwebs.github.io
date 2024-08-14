from flask import Flask, request, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

cmds = []


@app.route('/')
def index():
  return render_template('index.html', cmds=cmds)


@app.route('/submit', methods=['POST'])
def submit():
  input_text = request.form['inputText']
  cmds.append("> " + input_text)
  result = subprocess.run(input_text, shell=True, capture_output=True, text=True)
  cmds.append(result.stdout)
  redirect(url_for('index'))
  return render_template('index.html', cmds=cmds)


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)