from locust import HttpUser, task
import credentials as c

class LoginToApplication(HttpUser):
  @task
  def login(self):
    jsonData = {
      "user":{
        "email": c.USERNAME,
        "password": c.PASSWORD
        }
    }
    self.client.post(c.LNK_LOGIN, jsonData)
    

