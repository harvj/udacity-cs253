import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote=True)

heading = "<h2>Let's get our ROT13 on:</h2>"
form = """
<form method="post">
  <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
  <br>
  <input type="Submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hellow, Udacity!')

class Rot13Handler(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.write(form % {'text': text})

    def rot13(self, text):
        import string
        rot13 = string.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

        asciitext = text.decode('utf-8').encode('ascii', 'ignore')
        result = string.translate(asciitext, rot13)
        return escape_html(result)

    def get(self):
        self.response.write(heading)
        self.write_form()

    def post(self):
        self.response.write(heading)
        text = self.request.get('text')
        text = self.rot13(text)
        self.write_form(text)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/rot13', Rot13Handler)],
                              debug=True)
