from locust import HttpUser, task
import credentials as c

class HomePage(HttpUser):
  @task
  def home_page(self):
    self.client.get(c.LNK_HOME)
