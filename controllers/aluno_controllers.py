import json
from models.cachorro_models import cachorro   
from db import db                        
from flask import make_response

def get_cachorro():
    cachorro = cachorro.query.all()  
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de cachorro.',
            'dados': [cachorro.json() for cachorro in cachorro]  
        }, ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json'  
    return response

def get_cachorro_by_id(cachorro_id):
    cachorro = cachorro.query.get(cachorro_id)  

    if cachorro: 
        response = make_response(
            json.dumps({
                'mensagem': 'cachorro encontrado.',
                'dados': cachorro.json()  
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    else:
        
        response = make_response(
            json.dumps({'mensagem': 'cachorro não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
        
def create_cachorro(cachorro_data):           
    novo_cachorro = cachorro(  
                       
        nome=cachorro_data['nome'],     
        raca=cachorro_data['raca'],       
        idade=cachorro_data['idade']
                             
    )
    db.session.add(novo_cachorro)          
    db.session.commit()                  
    response = make_response(            
        json.dumps({                      
            'mensagem': 'cachorro cadastrado com sucesso.',  
            'cachorro': novo_cachorro.json()   
        }, sort_keys=False)               
    )
    response.headers['content-Type'] = 'application/json'  
    return response                      

