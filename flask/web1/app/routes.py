__author__ = 'uv2sun'
from myapp import fapp
from flask import render_template


@fapp.route('/')
def root():
    print('///////')
    return render_template('index.html')
