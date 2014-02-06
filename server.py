#!/usr/bin/env python
from flask import Flask
from flask import request, session, url_for, render_template
import json

from tweet2bibTeX import tweet2bibTeX

app = Flask( __name__, static_folder='static', static_url_path='/static' )

@app.route( "/", methods = ['POST', 'GET'] )
def hello():
    if request.method == 'GET' :
        return render_template( 'index.html' )
    if request.method == 'POST' :
        bib = tweet2bibTeX( request.form['tweeturl'] )
        if bib :
            return json.dumps(bib)
        else :
            return( "Couldn't find tweet.", 405 )

if __name__ == "__main__":
    app.run()
