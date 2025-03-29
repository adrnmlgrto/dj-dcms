from django.http import HttpResponseRedirect


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, redirect_to, *args, **kwargs):
        super().__init__(redirect_to, *args, **kwargs)
        self['HX-Redirect'] = self['Location']
        self.status_code = 200
