class Controller(object):

    def __init__(self, request):
        self.request = request
        self._unpack_request()

    def _unpack_request(self):
        for name, value in self._request_args().items():
            setattr(self, name, value)

    def _request_args(self):
        return {
            'POST': self.request.POST,
            'GET': self.request.GET,
            'matchdict': self.request.matchdict,
            'settings': self.request.registry['settings'],
            'db': self.request.registry['db'],
        }

    def __call__(self):
        data = self.make() or {}
        return data

    def make(self):
        pass
