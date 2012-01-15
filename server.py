from flask import Flask, url_for, render_template
from terminal import Terminal

app = Flask(__name__)
shellinabox = Terminal()

@app.route('/terminal')
def terminal():
  return render_template('terminal.html')

if __name__ == "__main__":
  if not shellinabox.process:
    shellinabox.start()
  
  app.debug = True
  app.run(port=5001)
