class Repository(object):
    def __init__(self, adapter=None):
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)

    def find(self, selector):
        return self.client.find_one(selector)

    def create(self, selector):
        return self.client.create(selector, kudo)

    def delete(self, selector):
        return self.client.delete(selector, kudo)

