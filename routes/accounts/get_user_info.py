import xor
from typing import TYPE_CHECKING
if TYPE_CHECKING: from context import Context
import time
from flask import request
import formats
import random
import sqlite3 as sqlite

def setup(ctx: 'Context'):
    app = ctx.app
    db = ctx.db
    get_arg = ctx.get_arg

    get_user_query = f"SELECT * FROM users WHERE extID = ?"

    def get_user(ext_id):
        try:
            return_ = db.execute(get_user_query, [ext_id]).fetchall()[0]
        except IndexError:
            return_ = None
        return return_

    @app.route('/getGJUserInfo20.php', methods=['GET', 'POST'])
    def get_user_info():
        ext_id = get_arg('targetAccountID')
        acc_id = get_arg('accountID')
        me = 0 # great naming
        if acc_id:
            me = int(acc_id)
            if not ctx.check_acc_pw(me, get_arg('gjp')):
                return '-1'
        if ext_id.isnumeric():
            ext_id = int(ext_id)
        try:
            user = get_user(ext_id)
        except sqlite.OperationalError:
            # Table code is from Cvolton's GMDPrivateServer thank you Cvolton!!!
            user = db.execute(
"""
CREATE TABLE users (
    isRegistered int(11) NOT NULL,
    userID int(11) NOT NULL,
    extID varchar(100) NOT NULL,
    userName varchar(69) NOT NULL DEFAULT 'undefined',
    stars int(11) NOT NULL DEFAULT '0',
    demons int(11) NOT NULL DEFAULT '0',
    icon int(11) NOT NULL DEFAULT '0',
    color1 int(11) NOT NULL DEFAULT '0',
    color2 int(11) NOT NULL DEFAULT '3',
    color3 int(11) NOT NULL DEFAULT '0',
    iconType int(11) NOT NULL DEFAULT '0',
    coins int(11) NOT NULL DEFAULT '0',
    userCoins int(11) NOT NULL DEFAULT '0',
    special int(11) NOT NULL DEFAULT '0',
    gameVersion int(11) NOT NULL DEFAULT '0',
    secret varchar(69) NOT NULL DEFAULT 'none',
    accIcon int(11) NOT NULL DEFAULT '0',
    accShip int(11) NOT NULL DEFAULT '0',
    accBall int(11) NOT NULL DEFAULT '0',
    accBird int(11) NOT NULL DEFAULT '0',
    accDart int(11) NOT NULL DEFAULT '0',
    accRobot int(11) DEFAULT '0',
    accGlow int(11) NOT NULL DEFAULT '0',
    accSwing int(11) NOT NULL DEFAULT '0',
    accJetpack int(11) NOT NULL DEFAULT '0',
    dinfo varchar(100) DEFAULT '',
    sinfo varchar(100) DEFAULT '',
    pinfo varchar(100) DEFAULT '',
    creatorPoints double NOT NULL DEFAULT '0',
    IP varchar(69) NOT NULL DEFAULT '127.0.0.1',
    lastPlayed int(11) NOT NULL DEFAULT '0',
    diamonds int(11) NOT NULL DEFAULT '0',
    moons int(11) NOT NULL DEFAULT '0',
    orbs int(11) NOT NULL DEFAULT '0',
    completedLvls int(11) NOT NULL DEFAULT '0',
    accSpider int(11) NOT NULL DEFAULT '0',
    accExplosion int(11) NOT NULL DEFAULT '0',
    chest1time int(11) NOT NULL DEFAULT '0',
    chest2time int(11) NOT NULL DEFAULT '0',
    chest1count int(11) NOT NULL DEFAULT '0',
    chest2count int(11) NOT NULL DEFAULT '0',
    isBanned int(11) NOT NULL DEFAULT '0',
    isCreatorBanned int(11) NOT NULL DEFAULT '0'
)""") # probably shouldnt just keep this in the script and put it in a file or somethinhg but oh whatever i can do it later
            user = get_user(ext_id)
            
        if user is None: return '-1'

        # placeholders
        # TODO: do whatever cvolton does for these https://github.com/Cvolton/GMDprivateServer/blob/master/incl/profiles/getGJUserInfo.php
        creator_points = 0
        rank = 1
        freq_state = 0
        msg_state = 0
        comment_state = 0
        badge = 0
        friend_requests = 0
        messages = 0
        friends = 0
        friend_state = 0
        if False: # enable for some fun
            user.update({
                'acc_icon': random.randint(0, 142),
                'acc_ship': random.randint(0, 51),
                'acc_ball': random.randint(0, 43),
                'acc_wave': random.randint(0, 35),
                'acc_ufo': random.randint(0, 35),
                'acc_robot': random.randint(0, 26),
                'acc_spider': random.randint(0, 17),
                'color1': random.randint(0, 42),
                'color2': random.randint(0, 42),
                'acc_glow': 0
            })
        return formats.get_user_info(user, {
            'creator_points': creator_points,
            'msg_state': msg_state,
            'freq_state': freq_state,
            'comment_state': comment_state,
            'rank': rank,
            'badge': badge,
            'youtube': '',
            'twitter': '',
            'twitch': '',
            'pms': messages,
            'requests': friend_requests,
            'friends': friends
        })
