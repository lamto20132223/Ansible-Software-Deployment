from sql_alchemy_learn import db, Node_Base, Column, relationship

class Node(Node_Base):
    __tablename__ = 'nodes'
    node_id = Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = Column(db.DateTime)
    updated_at = Column(db.DateTime)
    deleted_at = Column(db.DateTime)
    management_ip = Column(db.String(255))
    ssh_user = Column(db.String(255))
    ssh_password = Column(db.String(255))
    status = Column(db.Text)
    node_display_name = Column(db.String(255))
    node_info_id = Column(db.String(255), db.ForeignKey('node_infos.node_info_id'))
    deployment_id = Column(db.Integer, db.ForeignKey('deployments.deployment_id'))
    node_type = Column(db.String(255))

    node_info = relationship("Node_info")
    deployment = relationship("Deployment")
    service_infos = relationship("Service_info", back_populates="node")
    node_roles = relationship("Node_role", back_populates="node")

    def __repr__(self):
        return "<Node(node_id='%s',created_at='%s',updated_at='%s',deleted_at='%s',management_ip='%s',ssh_user='%s',ssh_password='%s',status='%s',node_display_name='%s',node_info_id='%s',deployment_id='%s',node_type='%s')>" % (
        self.node_id, self.created_at, self.updated_at, self.deleted_at, self.management_ip, self.ssh_user,
        self.ssh_password, self.status, self.node_display_name, self.node_info_id, self.deployment_id, self.node_type)

