from sql_alchemy_learn import db, Node_Base, Column, relationship

class Update_change(Node_Base):
    __tablename__ = 'update_change'
    id = Column(db.Integer,primary_key=True, autoincrement=True)
    update_id=Column(db.String(255), db.ForeignKey('updates.update_id'))
    change_id= Column(db.String(255), db.ForeignKey('changes.change_id'))
    def __repr__(self):
        return "<Update_change(update_id='%s',change_id='%s')>" %(self.update_id,self.change_id) 

