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
    name = db.StringProperty(required = True)
    cpf = db.StringProperty(required = True)
    fone = db.StringProperty(required = True)
    end = db.StringProperty(required = True)

class Livro(db.Model):
    titulo = db.StringProperty(required = True)
    autor = db.StringProperty(required = True)
    editora = db.StringProperty(required = True)
    ano = db.StringProperty(required = True)
	
class CadastroClienteHandler(Handler):
    def get(self):
		self.render('cadastrocliente.html')
		
    def post(self):
        name = self.request.get('nome')
        cpf = self.request.get('cpf')
        fone = self.request.get('fone')
        end = self.request.get('end')
		
		
        if name and cpf and fone and end:
            user = User(name = name, cpf = cpf, fone = fone, end = end)
            user.put()
            self.redirect( '/cadastrocliente' )
				

        else:
            self.response.out.write( 'Erro: Ocorreu um erro no cadastro do usuario!' )
			
		
		

class CadastroLivroHandler(Handler):
    def get(self):
        self.render('cadastrolivro.html')

    def post(self):
        titulo = self.request.get('titulo')
        autor = self.request.get('autor')
        editora = self.request.get('editora')
        ano = self.request.get('ano')

        if titulo and autor and editora and ano:
            livro = Livro(titulo = titulo, autor = autor, editora = editora, ano = ano)
            livro.put()
            self.redirect( '/cadastrolivro' )
                

        else:
            self.response.out.write( 'Erro: Ocorreu um erro no cadastro do livro!' )

	
class MainHandler(Handler):

    def get(self):
        self.render('index.html')

class LivrosHandler(Handler):

    def get(self):
        self.render('livros.html')


    
app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/l', LivrosHandler)
    ('/cadastrocliente', CadastroClienteHandler)
    ('/cadastrolivro', CadastroLivroHandler)
], debug=True)


