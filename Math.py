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

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	site.run(host="0.0.0.0", port=port, threaded=True)
