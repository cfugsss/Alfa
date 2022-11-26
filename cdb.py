import sqlite3

class oneUser:
    def __init__(self):
        self.conn = sqlite3.connect("cfugsb.db")
        self.curs = self.conn.cursor()

    def getDetails(self, name):
        self.curs.execute("SELECT * FROM users where username = ?", [name])
        userDetails = self.curs.fetchone()
        self.username = userDetails[1]
        self.password = userDetails[2]
        self.email = userDetails[3]
        self.balance = userDetails[4]
        return userDetails

        

    def createUser(self, username, password, email, balance):
        self.curs.execute(
            "INSERT INTO users (username, password, email, balance)" "VALUES(?,?,?,?)", (username, password, email, balance)
        )
        self.conn.commit()

    def confirm(self, username, password):
        self.curs.execute("SELECT * FROM users where username = ?", [username])
        account = self.curs.fetchone()
        try:
            if account[1] is None:
                return 2
        except TypeError:
            return 2
        if username == account[1] and password == account[2]:
            return 1
        else:
            return 3
