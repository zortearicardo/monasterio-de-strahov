import webapp2
import hashlib

mainForm = """
<html>
  <head>
    <title>Hello!</title>
  </head>
  <body>
    <form method="post">
    <h1>Monasterio de Strahov</h1>

    <label> 





    
      <input type="text" name="password">
      </label>
      <input type="submit">
      
    </form>
  </body>
</html>
"""

responseForm = """
<html>
  <head>
    <title>BashWiki</title>
  </head>
  <body>
    <p>%(password)s criptografado usando sha256: %(cypher)s</p>
  </body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write( mainForm )
    def post(self):
        password = self.request.get('password')
        self.response.out.write( responseForm % 
            { 'password': password, 'cypher': hashlib.sha512( password ).hexdigest() } )


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


