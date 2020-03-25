from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid
class Node_info(Node_Base):
    __tablename__ = 'node_infos'

    node_info_id = Column(db.String(255),primary_key=True,default=generate_uuid)
    node_name=Column(db.String(255))
    memory_mb = Column(db.Integer)
    memory_mb_free= Column(db.Integer)
    numa_topology= Column(db.Text)
    metrics=Column(db.Text)
    processor_core=Column(db.Integer)
    processor_count=Column(db.Integer)
    processor_threads_per_core=Column(db.Integer)
    processor_vcpu=Column(db.Integer)

    os_family=Column(db.String(255))
    pkg_mgr=Column(db.String(255))
    os_version=Column(db.String(255))
    default_ipv4=Column(db.String(255))
    default_broadcast=Column(db.String(255))
    default_gateway=Column(db.String(255))
    default_interface_id=Column(db.String(255))

    interface_resources=relationship("Interface_resource", back_populates="node_info")
    disk_resources = relationship("Disk_resource", back_populates="node_info")




    def __repr__(self):
        return "<Node_info(node_info_id='%s',node_name='%s',memory_mb='%s',memory_mb_free='%s',numa_topology='%s',metrics='%s',processor_core='%s',processor_count='%s',processor_threads_per_core='%s',processor_vcpu='%s',os_family='%s',pkg_mgr='%s',os_version='%s',default_ipv4='%s',default_broadcast='%s',default_gateway='%s',default_interface_id='%s')>" %(self.node_info_id,self.node_name,self.memory_mb,self.memory_mb_free,self.numa_topology,self.metrics,self.processor_core,self.processor_count,self.processor_threads_per_core,self.processor_vcpu,self.os_family,self.pkg_mgr,self.os_version,self.default_ipv4,self.default_broadcast,self.default_gateway,self.default_interface_id) 
