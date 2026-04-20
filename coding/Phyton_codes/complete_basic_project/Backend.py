import sqlite3 as sql

class TransactionObject():
    database = "clients.db"
    connection = None
    cursor = None
    connected = False

    def connect(self):
        TransactionObject.connection = sql.connect(TransactionObject.database)
        TransactionObject.cursor = TransactionObject.connection.cursor()
        TransactionObject.connected = True 

    def disconnect(self):
        TransactionObject.connection.close()
        TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cursor.execute(sql)
            else:
                TransactionObject.cursor.execute(sql,parms)
            return True
        else:
            return False
        
    def fetchall(self):
        return TransactionObject.cursor.fetchall()
    
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.connection.commit()
            return True
        else:
            return False
        
def initDB(self):
    trans = TransactionObject()
    trans.connect()

    trans.execute("CREATE TABLE IF NOT EXISTS clients(id INTEGER PRIMARY KEY, name TEXT, secondName TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.disconnect()

def insert(name, secondName, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clients VALUES(NULL, ?,?,?,?)", (name, secondName, email, cpf))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clients")
    rows = trans.fetchall()
    trans.disconnect()
    return rows
    
def search(name = "", secondName = "", email = "", cpf = ""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clients WHERE name = ? or secondName = ? or email = ? or cpf = ?", (name, secondName,email,cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows
    
def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clients WHERE id = ?",(id))
    trans.persist()
    trans.disconnect()
    
def update(id, name, secondName, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE clients SET nome = ?, secondName = ?, email = ?, cpf = WHERE id = ?", (name,secondName,email,cpf,id))
    trans.persist()
    trans.disconnect()

