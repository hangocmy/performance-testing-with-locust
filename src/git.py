from locust import HttpUser, task

class VisitGit(HttpUser):
  @task
  def hello_world(self):
    self.client.get("/hangocmy")