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

        - more commits!
        - collaborated with others!
        - feature branching
        - intentinal collision
    </pre>
    <footer> Useful links:
    <ul>
        <li><a href="https://github.com/github/gitignore">.gitignore</a> </li>
        <li><a href="https://www.gitkraken.com/git-client">GitKraken</a> </li>
        <li><a href="https://www.sourcetreeapp.com/">SourceTree</a> </li>
        <li><a href="https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">Authentication via SSH</a></li>
    </ul>
    </footer>
    '''

if __name__ == '__main__':
    serve(app)
