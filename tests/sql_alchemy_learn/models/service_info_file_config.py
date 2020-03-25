from sql_alchemy_learn import db, Node_Base, Column, relationship

class Service_info_File_config(Node_Base):
    __tablename__ = 'service_info_file_config'
    id = Column(db.Integer,primary_key=True, autoincrement=True)
    service_id=Column(db.Integer, db.ForeignKey('service_infos.service_id'))
    file_config_id= Column(db.Integer, db.ForeignKey('file_configs.file_id'))


    def __repr__(self):
        return "<Service_info_File_config(service_id='%s',file_config_id='%s')>" %(self.service_id,self.file_config_id) 





