from locust import HttpUser, task, between

class ArticleUser(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def get_article(self):
        self.client.get("/api/article/1")

    @task
    def add_article(self):
        self.client.post("/api/article/", json={"title":"测试标题"})
