from locust import HttpUser, task

class Setting(HttpUser):
  @task
  def setting(self):
    jsonData = {
      "profile": {
        "username": "hangocmy",
        "bio": "My nè",
        "image": "https://api.realworld.io/images/smiley-cyrus.jpeg",
        "following": false
      }
    }
    #self.client.post(c.LNK_LOGIN, jsonData)
    self.client.post('/api/profiles/hangocmy', jsonData)
    

