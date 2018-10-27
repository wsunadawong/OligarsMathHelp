#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:12:57 2018

@author: Warren
"""

from flask import Flask, render_template, request, redirect
import os
import requests
site = Flask(__name__)
@site.route('/')
def home():
    return render_template('Math.html')

@site.route('/algebra')
def algebra():
    return render_template('Algebra.html')

@site.route('/vertex')
def vertex():
    return render_template('Vertex.html')

@site.route('/quadratic')
def quadratic():
    return render_template('Quadratic.html')

@site.route('/geometry')
def geometry():
    return render_template('geometry.html')

@site.route('/vectors')
def vectors():
    return render_template('vectors.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	site.run(host="0.0.0.0", port=port, threaded=True)
