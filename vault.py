from telnetlib import ENCRYPT
from tkinter import END, simpledialog
from database import init_database
import hashlib

import mysql.connector

class VaultMethods:

    def __init__(self):
        self.db, self.cursor = init_database()

    def popup_entry(self, heading):
        answer = simpledialog.askstring("Enter details", heading)
        return answer

    def add_password(self, vault_screen):
        platform = self.popup_entry("Platform")
        userid = self.popup_entry("Username/Email")
        password = self.popup_entry("Password")
        # password=self.encrypt_password(password)
        # print("INSERT INTO passwords VALUES (\""+userid+"\" , \""+ password +"\" , \""+platform+"\")")
        insert_cmd = "INSERT INTO passwords VALUES (\""+platform+"\" , \""+ userid +"\" , \""+password+"\")"
        self.cursor.execute(insert_cmd)
        self.db.commit()
        vault_screen()

    def update_password(self, id, vault_screen):
        password = self.popup_entry("Enter New Password")
        print("UPDATE passwords SET password =\""+password+"\"  WHERE user_id = \""+id+"\"")
        self.cursor.execute(
            "UPDATE passwords SET password =\""+password+"\"  WHERE user_id = \""+id+"\"")

        self.db.commit()
        self.cursor.execute("SELECT * FROM password_manager.passwords")
        array = self.cursor.fetchall()
        print(array)
        # label.delete(0,END)
        vault_screen()

    def remove_password(self, id, vault_screen):
        self.cursor.execute("DELETE FROM passwords WHERE user_id = \""+ id +"\"")
        self.db.commit()
        vault_screen()

    def encrypt_password(self, password):
        password = password.encode("utf-8")
        encoded_text = hashlib.md5(password).hexdigest()
        return encoded_text
