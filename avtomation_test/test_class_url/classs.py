class Stend():
    def __init__(self, protocol='http', host='127.0.0.1', port='8080'):
        self.protocol = protocol
        self.host = host
        self.port = port

    def get_stend(self):
        return self.protocol + '://' + self.host + ':' + self.port


class Api():
    def __init__(self, post_books='/api/books/create'):
        self.post_books = post_books

    def get_api(self):
        return self.post_books

