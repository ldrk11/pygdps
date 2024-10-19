# Table code is from Cvolton's GMDprivateServer. thank you Cvolton!!!
def create_users_table(db):
    db.execute(
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
    )""")