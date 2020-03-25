from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid
class Update(Node_Base):
    __tablename__ = 'updates'
    update_id = Column(db.String(255),primary_key=True,default=generate_uuid)
    created_at=Column(db.DateTime)
    deleted_at= Column(db.DateTime)
    note=Column(db.Text)
    log=Column(db.Text)

    change=relationship('Update',secondary='update_change')
    def __repr__(self):
        return "<Update(update_id='%s',created_at='%s',deleted_at='%s',note='%s',log='%s')>" %(self.update_id,self.created_at,self.deleted_at,self.note,self.log) 


# def create_Update_Object(note):
#     update = Update(created_at=datetime.now(), deleted_at=None, note=note)
#
#     return update
