from locust import HttpUser, task, TaskSet
import json
import credentials as c

class LoginToApplication(HttpUser):
  def __init__(self, parent):
    super(LoginToApplication, self).__init__(parent)

    self.token = ""
    self.headers = {}  
  
  
  def on_start(self):
    self.token = self.login()
    self.headers = {'Authorization': 'Token ' + self.token}
      
  def login(self):
    jsonData = {
      "user":{
        "email": c.USERNAME,
        "password": c.PASSWORD
        }
    }

    res = self.client.post('/api/users/login', jsonData)
    return json.loads(res._content)['key']



