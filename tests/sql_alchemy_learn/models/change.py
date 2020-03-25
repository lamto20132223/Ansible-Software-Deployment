from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid
class Change(Node_Base):
    __tablename__ = 'changes'
    change_id=Column(db.String(255),primary_key=True,default=generate_uuid)
    created_at=Column(db.DateTime)
    finished_at=Column(db.DateTime)
    status=Column(db.String(255))
    change_type=Column(db.String(255))
    new_service=Column(db.String(255))
    backup_service=Column(db.String(255))
    new_file=Column(db.Text)
    backup_file=Column(db.Text)
    new_folder=Column(db.Text)
    backup_folder=Column(db.Text)
    change_log=Column(db.Text)
    task_id=Column(db.Integer, db.ForeignKey('tasks.task_id'))
    change_index=Column(db.Integer)
    file_config_id=Column(db.String(255), db.ForeignKey('file_configs.file_id'))
    file_config_file_id=Column(db.Integer)

    task = relationship("Task")
    file_config = relationship("File_config")
    update=relationship("Update", secondary='update_change')
    def __repr__(self):
        return "<Change(change_id='%s',created_at='%s',finished_at='%s',status='%s',change_type='%s',new_service='%s',backup_service='%s',new_file='%s',backup_file='%s',new_folder='%s',backup_folder='%s',change_log='%s',task_id='%s',change_index='%s',file_config_id='%s',file_config_file_id='%s')>" %(self.change_id,self.created_at,self.finished_at,self.status,self.change_type,self.new_service,self.backup_service,self.new_file,self.backup_file,self.new_folder,self.backup_folder,self.change_log,self.task_id,self.change_index,self.file_config_id,self.file_config_file_id) 



