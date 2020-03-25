import sqlalchemy as db 
import json

CONF = {"database":{"connection":"mysql+pymysql://lamtv10:lamtv10@172.16.29.198/lamtv10"}}
db_engine = db.create_engine(CONF["database"]["connection"])
db_connection = db_engine.connect()
db_metadata = db.MetaData()
db_nodes = db.Table('nodes', db_metadata, autoload=True, autoload_with=db_engine)

result = db_connection.execute("select * from nodes")
print(result)

#db_connection.execute(db_nodes.insert(), {"id: "})
