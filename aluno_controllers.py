import json
from models.aluno_models import aluno   
from db import db                        
from flask import make_response

def get_aluno():
    aluno = aluno.query.all()  
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de aluno.',
            'dados': [aluno.json() for aluno in aluno]  
        }, ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json'  
    return response

def get_aluno_by_id(aluno_id):
    aluno = aluno.query.get(aluno_id)  

    if aluno: 
        response = make_response(
            json.dumps({
                'mensagem': 'aluno encontrado.',
                'dados': aluno.json()  
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    else:
        
        response = make_response(
            json.dumps({'mensagem': 'aluno não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
        
def create_aluno(aluno_data):           
    novo_aluno = aluno(  
                       
        nome=aluno_data['nome'],     
        raca=aluno_data['raca'],       
        idade=aluno_data['idade']
                             
    )
    db.session.add(novo_aluno)          
    db.session.commit()                  
    response = make_response(            
        json.dumps({                      
            'mensagem': 'aluno cadastrado com sucesso.',  
            'aluno': novo_aluno.json()   
        }, sort_keys=False)               
    )
    response.headers['content-Type'] = 'application/json'  
    return response                      

