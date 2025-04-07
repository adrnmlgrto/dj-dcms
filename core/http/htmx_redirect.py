from django.http import HttpResponseRedirect

class HTTPResponseHXRedirect(HttpResponseRedirect):
    """
    HTMX-friendly redirect response that sets HX-Redirect header.

    Usage:
    ```
    return HTTPResponseHXRedirect("/target-url/")
    ```
    """
    status_code = 200

    def __init__(self, redirect_to: str, *args, **kwargs):
        super().__init__(redirect_to, *args, **kwargs)
        self.headers["HX-Redirect"] = self.headers["Location"]
        del self.headers["Location"]
