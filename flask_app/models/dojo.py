from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    DB = 'dojos_and_ninjas'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (id,name) VALUES (%(name)s);"
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def show_dojos_with_ninjas(cls,data):
        query = """SELECT * FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojo_id = dojos.id"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

