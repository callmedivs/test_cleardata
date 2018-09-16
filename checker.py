from flask import Flask, request
from checkString.checkStr import *

app = Flask(__name__)


@app.route('/test/', methods=[ 'GET'])
@app.route('/test/<path:input_str>',  methods=['GET'])
def string_checker(input_str=''):
    # create instance of the class CheckStr to use str_checker method
    str_checker = CheckStr()
    if input_str:
        pass
    else:
        input_str = request.args.get('input_str')
    return str(str_checker.check_alpha(input_str))

