from sql_alchemy_learn import db, Node_Base, Column, relationship
class Deployment(Node_Base):
    __tablename__ = 'deployments'
    deployment_id = Column(db.Integer,primary_key=True, autoincrement=True)
    created_at=Column(db.DateTime)
    updated_at= Column(db.DateTime)
    finished_at=Column(db.DateTime)
    status=Column(db.String(255))
    name=Column(db.String(255))
    jsondata=Column(db.Text)
    log=Column(db.Text)
    result=Column(db.String(255))
    progress=Column(db.String(255))
    service_setups = relationship("Service_setup", back_populates="deployment")
    node=relationship("Node", uselist=False, back_populates="deployment")
    def __repr__(self):
        return "<Deployment(deployment_id='%s',created_at='%s',updated_at='%s',finished_at='%s',status='%s',name='%s',jsondata='%s',log='%s',result='%s',progress='%s')>" %(self.deployment_id,self.created_at,self.updated_at,self.finished_at,self.status,self.name,self.jsondata,self.log,self.result,self.progress) 