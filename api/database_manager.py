import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_config import save_config, get_config, DATABASE_CONFIG_FILE
from database import models


class DatabaseManager:
    def __init__(self):
        self.load_db_config()
        self.databases = dict(sqlite=self.__generate_sqlite_connect_url, 
                              mysql=self.__generate_mysql_connect_url,
                              postgres=self.__generate_postgres_connect_url)
        

    def get_available_databases(self):
        return list(self.databases.keys())
    
    def connect_database(self, name=None, **kwargs):
        if name:
            func = self.databases[name]
            connect_url = func(**kwargs)
        else:
            func = self.databases[self.config['name']]
            connect_url = self.config['connect_url']
        engine = create_engine(connect_url)
        models.Base.metadata.create_all(engine)
        #TODO can we create the database if it doesnt exist?
        return engine

    def __generate_sqlite_connect_url(self, filename):
        return 'sqlite:///{}'.format(filename)

    def __generate_mysql_connect_url(self, user, password, database, host='localhost', port=3306):    
        #TODO local socket
        return 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(user, password, host, port, database)

    def __generate_postgres_connect_url(self, user, password, database, host='localhost', port=5432): 
        #TODO local socket
        return 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)

    def save_db_config(self, name, args):
        self.config = dict(name=name, args=args)
        self.config['connect_url'] = self.databases[name](**args)
        save_config(DATABASE_CONFIG_FILE, self.config)

    def load_db_config(self):
        try:
            self.config = get_config(DATABASE_CONFIG_FILE)
        except:
            self.config = None

def main():
    manager = DatabaseManager()
    engine = manager.connect_database()
    Session = sessionmaker(bind=engine)
    session = Session()
    sensor = models.SensorMapping(uuid=str(uuid.uuid4().hex))
    session.add(sensor)
    session.commit()

if __name__ == "__main__": 
    main()