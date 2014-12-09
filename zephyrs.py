import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>hello,world</html>')

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)

