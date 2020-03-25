from sql_alchemy_learn import db, Node_Base, Column, relationship
class Node_role(Node_Base):
    __tablename__ = 'node_roles'
    id = Column(db.Integer,primary_key=True, autoincrement=True)
    role_name=Column(db.String(255))
    node_id= Column(db.Integer, db.ForeignKey('nodes.node_id'))
    node = relationship("Node")
    def __repr__(self):
        return "<Node_role(role_name='%s',node_id='%s')>" %(self.role_name,self.node_id) 
