import time
from typing import TYPE_CHECKING
if TYPE_CHECKING: from context import Context
from create_accounts_table import create_accounts_table
import sqlite3 as sqlite

def setup(ctx: 'Context'):
    app = ctx.app
    db = ctx.db
    db_client = ctx.db_client
    get_arg = ctx.get_arg
    get_counter = ctx.get_counter
    pw_hasher = ctx.pw_hasher

    @app.route('/accounts/registerGJAccount.php', methods=['GET', 'POST'])
    def register_account():
        user_name = get_arg('userName')
        password = get_arg('password')
        email = get_arg('email')
        if not user_name or not password or not email:
            return '-1'
        secret = get_arg('secret')
        
        # account with same name already exists
        try:
            if len(db.execute("SELECT userName=? from accounts", [user_name]).fetchall()) != 0:
                return '-2'
        except sqlite.OperationalError:
            create_accounts_table(db)
            if len(db.execute("SELECT userName=? from accounts", [user_name]).fetchall()) != 0:
                return '-2'

        db.execute(
            "INSERT INTO accounts (userName, password, email, registerDate) VALUES (?,?,?,?)",
            [user_name, pw_hasher.hash(password), email, time.time()]
        )
        db_client.commit()
        return '1'