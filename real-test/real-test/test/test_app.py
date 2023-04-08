import unittest
from app.app import app

class TestApp(unittest.TestCase):

    def test_welcome(self):
        with app.test_client() as client:
            response = client.get('/welcome')
            self.assertEqual(response.status_code, 200)

    def test_home(self):
        with app.test_client() as client:
            response = client.get('/home')
            self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        with app.test_client() as client:
            response = client.post('/register', data=dict(username='testuser', password='testpassword'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        with app.test_client() as client:
            response = client.post('/login', data=dict(username='example', password='password'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_search(self):
        with app.test_client() as client:
            response = client.post('/search', data=dict(searchresults='test'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_profile(self):
        with app.test_client() as client:
            response = client.get('/profile')
            self.assertEqual(response.status_code, 200)
    
    def test_profile_followers(self):
        with app.test_client() as client:
            response = client.get('/profile/followers')
            self.assertEqual(response.status_code, 200)
    
    def test_profile_following(self):
        with app.test_client() as client:
            response = client.get('/profile/following')
            self.assertEqual(response.status_code, 200)
    
    def test_profile_posts(self):
        with app.test_client() as client:
            response = client.get('/profile/posts')
            self.assertEqual(response.status_code, 200)
    
    def test_profile_create(self):
        with app.test_client() as client:
            response = client.post('/profile/create', data=dict(submit_button='submit'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            response = client.post('/profile/create', data=dict(submit_button='discard'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_comments(self):
        with app.test_client() as client:
            response = client.get('/comments')
            self.assertEqual(response.status_code, 200)
    
    def test_comments_new(self):
        with app.test_client() as client:
            response = client.post('/comments/new', data=dict(submit_button='submit'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            response = client.post('/comments/new', data=dict(submit_button='discard'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main() 