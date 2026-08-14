from db import db                      

class aluno(db.Model):                   
    __tablename__ = 'aluno'  

    id = db.Column(db.Integer, primary_key=True)          
    nome = db.Column(db.String(80), nullable=False)     
    cpf  = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)               

    def json(self):                                        
        return {
            'id': self.id,            
            'nome': self.nome,   
            'CPF ': self.cpf ,  
            'idade': self.idade                                   
        }