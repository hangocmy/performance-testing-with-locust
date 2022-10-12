from locust import HttpUser, task
import credentials as c
class Articles(HttpUser):
  @task
  def articles(self):
    data ={
      "article": {
        "tagList": [],
        "title": "Hello Locust",
        "description": "Locust is a load testing tool written in Python.",
        "body": "Locust post"
      }
    }
    self.client.post(c.LNK_ARTICLES, data)