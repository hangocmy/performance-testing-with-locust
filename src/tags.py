from locust import HttpUser, task
import credentials as c

class Tags(HttpUser):
  @task
  def tags(self):
    a = ['implementations', 'welcome']
    for i in a:
      res = self.client.get(c.LNK_ARTICLES+'?tag={i}&limit=10&offset=0'.format(i=i))  
      
    print("Response status code:", res.status_code)
    print("Response content:", res.text)