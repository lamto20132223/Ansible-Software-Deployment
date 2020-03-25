from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid
class Interface_resource(Node_Base):
    __tablename__ = 'interface_resources'
    interface_id = Column(db.String(255),primary_key=True,default=generate_uuid)
    device_name=Column(db.String(255))
    speed=Column(db.Integer)
    port_info=Column(db.Text)
    active=Column(db.String(255))
    features=Column(db.Text)
    macaddress=Column(db.String(255))
    module=Column(db.String(255))
    mtu=Column(db.Integer)
    pciid=Column(db.String(255))
    phc_index=Column(db.Integer)
    type_interface=Column(db.String(255))
    is_default_ip=Column(db.String(255))
    node_info_id=Column(db.String(255),db.ForeignKey('node_infos.node_info_id') )
    node_info = relationship("Node_info")
    def __repr__(self):
        return "<Interface_resource(interface_id='%s',device_name='%s',speed='%s',port_info='%s',active='%s',features='%s',macaddress='%s',module='%s',mtu='%s',pciid='%s',phc_index='%s',type_interface='%s',is_default_ip='%s',node_info_id='%s')>" %(self.interface_id,self.device_name,self.speed,self.port_info,self.active,self.features,self.macaddress,self.module,self.mtu,self.pciid,self.phc_index,self.type_interface,self.is_default_ip,self.node_info_id) 

