# PyGDPS [WIP]
Geometry dash Private server written in Python using Flask and Sqlite, highly based off [Cvolton/GMDprivateServer](https://github.com/Cvolton/GMDprivateServer)

## Running
Run `run.py`.

## Implemented
- `/getGJUserInfo.php` - works fine but creator points, rank and etc are hardcoded

## Was Implemented but needs to be changed to SQLite
- `/uploadGJLevel.php` - uploading a level works, and thats it (no replacing already uploaded level, etc)
- `/getGJLevels.php` - searching by difficulty is missing
- `/downloadGJLevel.php` - daily levels dont work yet
- `/accounts/registerGJAccount.php` - nothing much to say, it works (passwords are argon2 hashed)
- `/accounts/loginGJAccount.php` - same as above
- `/updateGJUserScore.php` - works fine
