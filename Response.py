class Response:

    def __init__(self, response):
        self.response = response
        self.json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        schema.model_validate(self.json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return f"""
            Status code: {self.response_status} 
            Requested url: {self.response.url}
            Response body: {self.json}
        """
