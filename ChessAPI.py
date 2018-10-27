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

@site.route('/player', methods = ['POST', 'GET'])
def player():
    if request.method == 'POST':
        playername = request.form
        player_url = 'https://api.chess.com/pub/player/' + playername['Player']
        player_data = requests.get(player_url).json()  
        if 'player_id' in player_data.keys():
            stat_data = requests.get(player_url + '/stats').json()
            return render_template('Player.html', player = playername, datas = player_data, stats = stat_data)
        else:
            return render_template('Nonexistent.html')
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	site.run(host="0.0.0.0", port=port, threaded=True)