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
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
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
    def get_one(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'id':dojo_id})
        one_dojo = cls(results[0])
        return one_dojo
    
    @classmethod
    def show_dojos_with_ninjas(cls,data):
        query = """SELECT * FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        dojo = cls(results[0])
        # Look at each row of the same dojo + ninjas and add each of those ninjas into our class "ninjas" list
        for dojo_row in results:
            # print (f"********************{ dojo_row }")
            ninja_data = {
                'id': dojo_row['ninjas.id'],
                'first_name': dojo_row['first_name'],
                'last_name': dojo_row['last_name'],
                'age': dojo_row['age'],
                'dojo_id': dojo_row['dojo_id'],
                'created_at': dojo_row['ninjas.created_at'],
                'updated_at': dojo_row['ninjas.updated_at'],
            }
            dojo.ninjas.append(ninja.Ninja( ninja_data ))
        return dojo

