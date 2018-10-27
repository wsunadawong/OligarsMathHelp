#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 09:12:57 2018

@author: Warren
"""

from flask import Flask, render_template, request, redirect
import os
import requests
site = Flask(__name__)
api_url = 'https://api.chess.com/pub/player/The20thDuck'
@site.route('/')
def home():
    return render_template('Home.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	site.run(host="0.0.0.0", port=port, threaded=True)
