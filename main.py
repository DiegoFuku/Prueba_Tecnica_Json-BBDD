import psycopg2 
import json

connection = psycopg2.connect(
    host= "localhost",
    user= "postgre",
    password= "secret",
    database= "universidad_db",
    port="5432"
)
connection.autocommit=True

def crear_tabla_universidad():
    cursor=connection.cursor()
    query="""CREATE TABLE IF NOT EXISTS university(
    id_university SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL); """
    cursor.execute(query)
    cursor.close()


def crear_tabla_pais():
    cursor=connection.cursor()
    query=""" CREATE table IF NOT EXISTS country(
    id_country SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL);"""
    cursor.execute(query)
    cursor.close()


def crear_tabla_ciudad():
    cursor=connection.cursor()
    query="""CREATE TABLE IF NOT EXISTS city(
    id_city SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    id_country INTEGER,
    CONSTRAINT fk_id_country
    FOREIGN KEY (id_country) REFERENCES
    country(id_country));"""
    cursor.execute(query)
    cursor.close()

def crear_tabla_person():
    cursor=connection.cursor()
    query="""Create table if not exists person(
    id_person SERIAL PRIMARY KEY,
    first_name varchar(50),
    last_name varchar (50),
    email varchar(100),
    gender varchar (50),
    city_id INTEGER,
    country_id INTEGER,
    university_id INTEGER,
    CONSTRAINT fk_city_id FOREIGN KEY (city_id) REFERENCES city(id_city),
    CONSTRAINT fk_country_id FOREIGN KEY (country_id) REFERENCES country(id_country),
    CONSTRAINT fk_university_id FOREIGN Key (university_id) REFERENCES university(id_university));"""
    cursor.execute(query)
    cursor.close()

def crear_tablas():
    crear_tabla_universidad()
    crear_tabla_pais()
    crear_tabla_ciudad()
    crear_tabla_person()

def insertar_universidad(uni):
    uni= uni.replace("'","")
    cursor=connection.cursor()
    query=f"""SELECT * from university where name = '{uni}';"""
    cursor.execute(query)
    if cursor.fetchone() is None:
        query=f"""INSERT INTO university (name) VALUES ('{uni}')"""
        cursor.execute(query)
    query=f"""SELECT * from university where name = '{uni}';"""
    cursor.execute(query)    
    id_university=cursor.fetchone()
    return (id_university[0])
    cursor.close() 

def insertar_pais(pais):
    cursor=connection.cursor()
    query=f"""SELECT * from country where name = '{pais}';"""
    cursor.execute(query)   
    if cursor.fetchone() is None:
        query=f"""INSERT INTO country (name) VALUES ('{pais}')"""
        cursor.execute(query)
    query=f"""SELECT * from country where name = '{pais}';"""
    cursor.execute(query)    
    id_pais=cursor.fetchone()
    return (id_pais[0])

def insertar_ciudad(city,country_id):
    city=city.replace("'"," ")
    cursor=connection.cursor()
    query=f"""SELECT * from city where name = '{city}';"""
    cursor.execute(query)
    if cursor.fetchone() is None:
        query=f"""INSERT INTO city (name,id_country) VALUES ('{city}','{country_id}')"""
        cursor.execute(query)
    query=f"""SELECT * from city where name = '{city}';"""
    cursor.execute(query)
    id_city=cursor.fetchone()
    return(id_city[0])   


def insertar_person(first,last,email,gender,city_id,country_id,universidad_id):
    last=last.replace("'"," ")
    print("first: ",first, "last: ",last, "email: ",email, "gender: ",gender)
    print("city_id: ",city_id)
    print("country_id: ",country_id)
    print("universidad_id: ",universidad_id) 
    
    cursor=connection.cursor()
    query=f"""INSERT INTO person (first_name,last_name,email,gender,city_id,country_id,university_id)
    VALUES ('{first}','{last}','{email}','{gender}','{city_id}','{country_id}','{universidad_id}');""" 
    cursor.execute(query)
    cursor.close()  

def leer_archivo():
    with open("univ.json") as f:
        data=json.load(f)        
        for j in data:            
            id_universidad = insertar_universidad(j["university"])
            id_pais= insertar_pais(j["Country"])
            id_city=insertar_ciudad(j["City"],id_pais) 
            insertar_person(j["first_name"],j["last_name"],j["email"],j["gender"],id_city,id_pais,id_universidad)                     
            
            
    f.close()    
if __name__=="__main__":
    crear_tablas() 
    leer_archivo()   
