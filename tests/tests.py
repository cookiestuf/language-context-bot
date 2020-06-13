import bot
import unittest
import sqlite3
import os

class TestDBMethods(unittest.TestCase):
    def setUp(self):
        bot.create_database("test")
        
    def tearDown(self):
        """
        Delete the database
        """
        os.remove("test.db")

    def test_setUp(self):
        """
        Setup a temporary database
        """
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        # get count of tables
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
        self.assertEqual(c.fetchone()[0], 1)
        conn.commit()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='words' ''')
        self.assertEqual(c.fetchone()[0], 1)
        conn.commit()
        c.close()
        conn.close()

    def test_getUsersForLanguage(self):
        """
        Tests that all users for given language are returned
        """
        bot.update_database("test",'users', ["123", 1,"english"])
        bot.update_database("test",'users', ["234", 1,"english"])
        bot.update_database("test",'users', ["345", 1,"english"])
        english= bot.get_users_for_language("english")
        spanish =bot.get_users_for_language("spanish")
        
        self.assertEqual(["123","234","345"], english)
        self.assertEqual([], spanish)

    def test_addNewUserWithLanguage(self):
        """
        check that new user with specified language exists in DB after adding
        """
    def test_addLanguagetoExistingUser(self):
        """
        check that existing user is not modifying except for new language after adding
        """
    def test_addUserWithoutLanguage(self):
        """
        check user exists in DB after adding user
        """
    def test_removeUser(self):
        return
    def test_removeLanguageFromUser(self):
        return

user1 = {"id":"6253282", 'lang':"English"}


