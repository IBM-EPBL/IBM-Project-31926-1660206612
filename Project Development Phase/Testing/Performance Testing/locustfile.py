from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    

    @task
    def about(self):
        self.client.get("/intro")
        
    @task 
    def image(self):
    	self.client.get("/image1")
    
    @task 
    def home(self):
    	self.client.get('/')
    	
    @task 
    def predict(self):
    	self.client.get('/predict')
