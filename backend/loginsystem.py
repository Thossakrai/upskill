import sqlite3


class LoginSystem(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.type = None

    def isValidUser(self):
        conn = sqlite3.connect('upskilldb.sqlite3')
        c = conn.cursor()
        c.execute('SELECT USERNAME FROM USERNAME_DETAIL WHERE USERNAME = ? AND PASSWORD = ?', (self.username, self.password))
        data = c.fetchone()
        if data == None :
            return None
        print(data)
        c.execute('SELECT UTYPE, UPREF FROM USER_DETAIL WHERE USERNAME = ?', (self.username,))
        utype = c.fetchone()
        conn.close()
        print("utype = ", utype)
        print(type(utype))
        print(utype[0], utype[1])
        return utype
