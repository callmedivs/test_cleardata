from flask import Flask, request
from checkString.checkStr import *

app = Flask(__name__)


@app.route('/<path:input_str>',  methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def string_checker(input_str=''):
    # create instance of the class CheckStr to use str_checker method
    str_checker = CheckStr()
    if request.method == 'POST':
        input_str = request.form['input_str']
    else:
        if input_str:
            pass
        else:
            input_str = request.args.get('input_str')

    return str(str_checker.check_alpha(input_str))

