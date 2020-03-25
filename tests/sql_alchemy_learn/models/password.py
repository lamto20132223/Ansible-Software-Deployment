from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid

class Password(Node_Base):
    __tablename__ = 'passwords'
    password_id = Column(db.String(255),primary_key=True,default=generate_uuid)
    created_at=Column(db.DateTime)
    updated_at= Column(db.DateTime)
    user=Column(db.String(255))
    password=Column(db.String(255))
    update_id=Column(db.String(255), db.ForeignKey('updates.update_id'))
    service_name=Column(db.String(255))

    update = relationship("Update")
    def __repr__(self):
        return "<Password(password_id='%s',created_at='%s',updated_at='%s',user='%s',password='%s',update_id='%s',service_name='%s')>" %(self.password_id,self.created_at,self.updated_at,self.user,self.password,self.update_id,self.service_name) 