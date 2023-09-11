
from pymongo.mongo_client import MongoClient

def conexion():
    uri = "mongodb+srv://sebas:1234@cluster0.axp2y2n.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)
    
 #Se utiliza para obtener los documentos de la conexión "data_real" de la base de datos MongoDB

def lecturaDatos():
    client = conexion()
    db = client.Actividad4.data_real
    data_list = []
    for data_real_bd in db.find():
        data_list.append(data_real_bd)
    return data_list
   