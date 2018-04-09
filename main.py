from flask import Flask, request #imports Flask class from flask module
from caesar import rotate_string

app = Flask(__name__) #app will be object created by the constructor Flask. _name_ is a varibale controlled by Python that tell code what module it's in.
app.config['DEBUG'] = True  #enables DEBUG configuration setting for Flask

form = """			
	<!DOCTYPE html>
	<html>
		<head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width:540px;
                    font: 16px sana-serif;
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
            <form method="POST">
                <label for = "rot"> Rotate characters by: </label>
                <input type = "text" name = "rot" value="0" id="rot" />
                <textarea type = "text" name="text" id="text"> {0} </textarea>
                <input type = "submit" value="Submit" />
            </form>
        </body>

    </html>            
"""

@app.route("/") #decorator that creates a mapping b/w the path('/' and the function we're about to define)
def index():    #INDEX; a function with zero variables
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    characters_encrypted = rotate_string (text, int(rot))
    return form.format(characters_encrypted)

app.run()   #passes control to Flask