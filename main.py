# Todd McCullough  June 29 2020

from flask import Flask
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import love_main as hpl

import functools
import numpy as np
import os
import pandas as pd
import re


theme = 'cappucino'


ailove = Flask(__name__, instance_relative_config=True)
ailove.config.from_mapping(
        SECRET_KEY='dev', # change to a random value later when deploying
        DATABASE=os.path.join(ailove.instance_path, 'main.sqlite'),
    )

@ailove.route('/index')
def index():


    return render_template('index.html',
    theme = theme)

if __name__ == "__main__":
    ailove.run()
