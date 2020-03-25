from sql_alchemy_learn import db, Node_Base, Column, relationship
class Service_info(Node_Base):
    __tablename__ = 'service_infos'
    service_id = Column(db.Integer,primary_key=True, autoincrement=True)
    service_type=Column(db.String(255))
    service_status=Column(db.String(255))
    tag=Column(db.String(255))
    node_id=Column(db.Integer, db.ForeignKey('nodes.node_id'))

    node = relationship("Node")
    file_configs = relationship("File_config",secondary='service_info_file_config')
   
    def __repr__(self):
        return "<Service_info(service_id='%s',service_type='%s',service_status='%s',tag='%s',node_id='%s')>" %(self.service_id,self.service_type,self.service_status,self.tag,self.node_id) 
