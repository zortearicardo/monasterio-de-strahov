import webapp2
import hashlib

mainForm = """
<html> 
<head> 
	<meta charset="utf-8" /> 	
	<title>Monasterio de Strahov</title>
</head> 
<body> 
<form name="meuForm" method="post" id="formulario"> 
	<div class="box"> 
		<h1>Cadastro de cliente:</h1>
	<label>
	<p> </p> 
			<span>Nome:</span> <input type="text" class="input_text" name="nome" id="name"/> 
	</label></br>
	<p> </p> 	
			<label> <span>Cpf:&nbsp&nbsp&nbsp &nbsp</span><input type="text" class="input_text" name="fone" id="fone"/> 
	</label> </br>
		<p> </p> 
			<label> <span>Fone:  &nbsp  </span> <input type="text" class="input_text" name="fone" id="fone"/> 
	</label> </br>
		<p> </p> 
			<label> <span>End:&nbsp&nbsp &nbsp</span> <input type="text" class="input_text" name="end" id="end"/> 
	</label> </br>
		<p> </p> 
			<input type="button" name="botao-ok" value="Confirmar">
			
			
			<h1>Cadastro De Livro:</h1>
	<label>
	<p> </p> 
			<span>Titulo:&nbsp</span> <input type="text" class="input_text" name="titulo" id="titulo"/> 
	</label></br>
		<p> </p> 
			<label> <span>Autor:&nbsp&nbsp&nbsp</span><input type="text" class="input_text" name="autor" id="autor"/> 
	</label> </br>
		<p> </p> 
			<label> <span>Editora:</span> <input type="text" class="input_text" name="editora" id="editora"/> 
	</label> </br>
		<p> </p> 
			<label> <span>Ano:&nbsp&nbsp &nbsp&nbsp</span> <input type="text" class="input_text" name="ano" id="ano"/> 
	</label> </br>
		<p> </p> 
			<input type="button" name="botao-ok" value="Confirmar">
		
		

	
	<label> 
			
	</label> 
	</div> 
</form>
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





