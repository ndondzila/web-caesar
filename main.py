from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rotation">Rotate by:</label>
            <input id="rotation" type="text" name="rot" value="0"</>
            <input type="submit" />
            <textarea name="text">{0}</textarea>
            
        </form>
    </body>

    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotation = int(request.form["rot"])
    message = request.form["text"]
    return form.format(rotate_string(message, rotation))
app.run()