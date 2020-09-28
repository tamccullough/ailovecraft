# Todd McCullough  June 29 2020

from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

import love_main as hpl

import numpy as np
import pandas as pd


theme = 'cappucino'

ailove = Flask(__name__)

@ailove.route('/index')
def index():
    generated_text = open('generated.txt','r')
    description = 'An Example of Generated Text'
    return render_template('index.html',
    generated_text = generated_text.read(), description = description,
    theme = theme)

@ailove.route('/generate', methods=['POST'])
def generate():
    sentence = request.form['generate']
    generated_text = hpl.generate_text(start_string=sentence+u'\n',temp=1.0)
    description = 'Generated Text Produced by the Model'
    return render_template('index.html',
    generated_text = generated_text, description = description,
    theme = theme)

if __name__ == "__main__":
    ailove.run()
