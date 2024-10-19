# Table code is mostly from Cvolton's GMDprivateServer. thank you Cvolton!!!
def create_accounts_table(db):
    db.execute("""
CREATE TABLE `accounts` (
    `userName` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    `gjp2` varchar(255) DEFAULT NULL,
    `email` varchar(255) NOT NULL,
    `accountID` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `isAdmin` int(11) NOT NULL DEFAULT '0',
    `mS` int(11) NOT NULL DEFAULT '0',
    `frS` int(11) NOT NULL DEFAULT '0',
    `cS` int(11) NOT NULL DEFAULT '0',
    `youtubeurl` varchar(255) NOT NULL DEFAULT '',
    `twitter` varchar(255) NOT NULL DEFAULT '',
    `twitch` varchar(255) NOT NULL DEFAULT '',
    `salt` varchar(255) NOT NULL DEFAULT '',
    `registerDate` int(11) NOT NULL DEFAULT '0',
    `friendsCount` int(11) NOT NULL DEFAULT '0',
    `discordID` bigint(20) NOT NULL DEFAULT '0',
    `discordLinkReq` bigint(20) NOT NULL DEFAULT '0',
    `isActive` tinyint(1) NOT NULL DEFAULT '0',
    `saveData` LONGTEXT NOT NULL DEFAULT '0',
    `saveKey` LONGTEXT NOT NULL DEFAULT '0'
)""")