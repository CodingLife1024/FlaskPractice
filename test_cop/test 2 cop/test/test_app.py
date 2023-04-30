import unittest
import sqlite3
from app.app import app, get_db_connection, get_user, get_post

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

        # connect to the database and create the posts table if it doesn't exist
        conn = get_db_connection()
        try:
            conn.execute('CREATE TABLE IF NOT EXISTS posts (post_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL, user_id INTEGER NOT NULL, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
            conn.commit()
        except sqlite3.Error as e:
            print('Database error while creating posts table:', e)
        finally:
            conn.close()

        # insert a sample post
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)', ('Test Post', 'Lorem ipsum dolor sit amet', 1))
            conn.commit()
        except sqlite3.Error as e:
            print('Database error while inserting sample post:', e)
        finally:
            conn.close()

    def test_get_db_connection(self):
        connection = get_db_connection()
        self.assertNotEqual(connection, None)

    def test_get_user(self):
        user_id = 1
        user = get_user(user_id)
        self.assertNotEqual(user, None)

    def test_get_post(self):
        post_id = 1
        post = get_post(post_id)
        self.assertNotEqual(post, None)

    def test_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        }
        response = self.app.post('/register', data=data)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.app.post('/login', data=data)
        self.assertEqual(response.status_code, 200)

    def test_timeline(self):
        response = self.app.get('/timeline')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        user_id = 1
        response = self.app.get(f'/profile/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_profileposts(self):
        user_id = 1
        response = self.app.get(f'/profileposts/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'title': 'Test Post',
            'content': 'Lorem ipsum dolor sit amet'
        }
        response = self.app.post('/create', data=data)
        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com'
        }
        response = self.app.post('/edit_profile', data=data)
        self.assertEqual(response.status_code, 200)
    
    def test_comments(self):
        post_id = 1
        response = self.app.get(f'/comments/{post_id}')
        if response.status_code != 200:
            print(f'Error: Failed to get comments for post {post_id}. Response status code: {response.status_code}')
            print(f'Response data: {response.data}')
        self.assertEqual(response.status_code, 200)

    # def test_comments(self):
    #     post_id = 1
    #     response = self.app.get(f'/comments/{post_id}')
    #     self.assertEqual(response.status_code, 200)

    def test_new_comment(self):
        data = {
            'post_id': 1,
            'content': 'Test comment'
        }
        response = self.app.post('/new_comment', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()