#!/usr/bin/env python


import os
import webapp2
import jinja2

from google.appengine.ext import db


#Jinja2 Directory Configuration
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


#Default Handler
class Handler(webapp2.RequestHandler):
    def get(self):
        users = db.GqlQuery('SELECT * FROM User')
        self.render('index.html',users = users)

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class User(db.Model):
    name = db.StringProperty( required = True )
    cpf = db.StringProperty(required = True)
	fone = db.StringProperty(required = True)
    end = db.StringProperty(required = True)

class Livro(db.Model):
	titulo = db.StringProperty(required = True)
	autor = db.StringProperty (required = True)
	editora = db.StringProperty (required = True)
	ano = db.StringProperty (required = True)
	
class CadastroHandler(Handler):
	def get(self):
		self.render('cadastro.html')
		
		def post(self):
        name = self.request.get('name')
        cpf = self.request.get('cpf')
		fone = self.request.get('fone')
		end = self.request.get('end')
		
		titulo = self.request.get('titulo')
		autor = self.request.get('autor')
		editora = self.request.get('editora')
		ano = self.request.get('ano')

        if name and cpf and fone and end:
            user = User(name = name, cpf = cpf, fone = fone, end = end)
            user.put()
			self.redirect( '/cadastro' )
				

        else:
            self.response.out.write( 'Erro: Ocorreu um erro no cadastro do usuario!' )
			
		
		 if titulo and autor and editora and ano:
            livro = Livro(titulo = titulo, autor = autor, editora = editora, ano = ano)
            livro.put()
			self.redirect( '/cadastro' )
				

        else:
            self.response.out.write( 'Erro: Ocorreu um erro no cadastro do livro!' )



	
class MainHandler(Handler):

    def get(self):
        self.render('index.html')


    
app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/cadastro', CadastroHandler)
], debug=True)


