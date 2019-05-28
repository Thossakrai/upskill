import sqlite3


class LoginSystem(object):
    def __init__(self, username, password):
        # conn = sqlite3.connect('../upskilldb.db')
        # c = conn.cursor()
        self.username = username
        self.password = password
        self.type = None

    def isValidUser(self):
        conn = sqlite3.connect('../upskilldb.db')
        c = conn.cursor()
        c.execute('SELECT USERNAME FROM USER WHERE USERNAME = ?', self.username)
