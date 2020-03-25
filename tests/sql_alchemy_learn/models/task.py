from sql_alchemy_learn import db, Node_Base, Column, relationship

class Task(Node_Base):
    __tablename__ = 'tasks'
    task_id = Column(db.Integer,primary_key=True, autoincrement=True)
    created_at=Column(db.DateTime)
    finished_at= Column(db.DateTime)
    task_display_name=Column(db.String(255))
    setup_data=Column(db.String(255))
    task_type=Column(db.String(255))
    status=Column(db.String(255))
    result=Column(db.String(255))
    log=Column(db.Text)
    task_index=Column(db.Integer)
    service_setup_id=Column(db.String(255), db.ForeignKey('service_setups.service_setup_id'))
    service_setup = relationship("Service_setup")
    changes = relationship("Change", back_populates="task")
    def __repr__(self):
        return "<Task(task_id='%s',created_at='%s',finished_at='%s',task_display_name='%s',setup_data='%s',task_type='%s',status='%s',result='%s',log='%s',task_index='%s',service_setup_id='%s')>" %(self.task_id,self.created_at,self.finished_at,self.task_display_name,self.setup_data,self.task_type,self.status,self.result,self.log,self.task_index,self.service_setup_id) 