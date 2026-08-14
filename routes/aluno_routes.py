
from flask import Blueprint, request                  
                                                      
from controllers.aluno_controllers import create_aluno, get_aluno
                                                      

aluno_routes = Blueprint('aluno_routes', __name__)    
                                                      

@aluno_routes.route('/Aluno', methods=['GET'])
def aluno_get():
    return get_aluno()

@aluno_routes.route('/Aluno', methods=['POST'])       
def aluno_post():                                    
    aluno_data = request.json                         
    return create_aluno(request.json)                 
