from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return '''<pre>
        Welcome!
        So far we learned:
        - git init
        - git status 
        - .gitignore
        - git add
        - git commit
        - git log
    </pre>'''

if __name__ == '__main__':
    serve(app)

