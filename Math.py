#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:12:57 2018

@author: Warren
"""

from flask import Flask, render_template, request, redirect
import os
import requests
import math

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

@site.route('/quadratic', methods = ['POST', 'GET'])
def quadratic():
    if request.method == 'POST':
	coefficients = request.form
	a = float(coefficients["a"])
	b = float(coefficients["b"])
	c = float(coefficients["c"])
	if b**2 - 4*a*c < 0:
		root1 = str(-b/(2*a)) + " + " + str(math.sqrt(4*a*c - b**2)/(2*a)) + "i"
		root2 = str(-b/(2*a)) + " - " + str(math.sqrt(4*a*c - b**2)/(2*a)) + "i"
	else:
		root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
		root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    	return render_template('Quadratic.html', root1 = root1, root2 = root2)
    else: 
	return render_template('Quadratic.html')

@site.route('/geometry')
def geometry():
    return render_template('Geometry.html')

@site.route('/vectors')
def vectors():
    return render_template('Vectors.html')



@site.route('/herons', methods = ['POST', 'GET'])
def herons():
    if request.method == 'POST':
	coefficients = request.form
	a = float(coefficients["a"])
	b = float(coefficients["b"])
	c = float(coefficients["c"])
	
		area = (math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c)))
		
    	return render_template('herons.html', area = area)
    else: 
	return render_template('herons.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	site.run(host="0.0.0.0", port=port, threaded=True)
