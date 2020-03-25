from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid
class Openstack_config(Node_Base):
    __tablename__ = 'openstack_configs'
    config_id = Column(db.String(255),primary_key=True,default=generate_uuid)
    created_at=Column(db.DateTime)
    deleted_at=Column(db.DateTime)
    key=Column(db.String(255))
    value=Column(db.Text)
    service=Column(db.String(255))
    update_id=Column(db.String(255), db.ForeignKey('updates.update_id'))
    password_id=Column(db.Integer, db.ForeignKey('passwords.password_id'))
    block=Column(db.String(255))
    file_id=Column(db.Integer, db.ForeignKey('file_configs.file_id'))
    activate=Column(db.Integer)

    update = relationship("Update")
    password = relationship("Password")
    file_config = relationship("File_config")

    def __repr__(self):
        return "<Openstack_config(config_id='%s',created_at='%s',deleted_at='%s',key='%s',value='%s',service='%s',update_id='%s',password_id='%s',block='%s',file_id='%s',activate='%s')>" %(self.config_id,self.created_at,self.deleted_at,self.key,self.value,self.service,self.update_id,self.password_id,self.block,self.file_id,self.activate) 