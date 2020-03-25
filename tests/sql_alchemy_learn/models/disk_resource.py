from sql_alchemy_learn import db, Node_Base, Column, relationship, generate_uuid
class Disk_resource(Node_Base):
    __tablename__ = 'disk_resources'
    disk_id = Column(db.String(255),primary_key=True,default=generate_uuid)
    device_name=Column(db.String(255))
    size= Column(db.Integer)
    model=Column(db.String(255))
    removable=Column(db.Integer)
    sectors=Column(db.Text)
    sectorsize=Column(db.Integer)
    serial=Column(db.String(255))
    vendor=Column(db.String(255))
    support_discard=Column(db.String(255))
    virtual=Column(db.Integer)
    node_info_id=Column(db.String(255), db.ForeignKey('node_infos.node_info_id'))

    node_info = relationship("Node_info")
    def __repr__(self):
        return "<Disk_resource(disk_id='%s',device_name='%s',size='%s',model='%s',removable='%s',sectors='%s',sectorsize='%s',serial='%s',vendor='%s',support_discard='%s',virtual='%s',node_info_id='%s')>" %(self.disk_id,self.device_name,self.size,self.model,self.removable,self.sectors,self.sectorsize,self.serial,self.vendor,self.support_discard,self.virtual,self.node_info_id) 

