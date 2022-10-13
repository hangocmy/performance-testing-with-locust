from locust import HttpUser, task
import credentials as c

class SignUpToApplication(HttpUser):
  @task
  def signup(self):
    jsonData = {
      "user":{
        "email": 'hangocmy00@gmail.com',
        "password": '123456',
        "username": "hangocmy"
        }
    }
    #self.client.post(c.LNK_LOGIN, jsonData)
    self.client.post('/api/users', jsonData)
    

