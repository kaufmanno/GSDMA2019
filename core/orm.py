from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, synonym, backref
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()


class BoreholeOrm(Base):
    """The Borehole table
    
    Attributes
    -----------
    id : str
         The id of the borehole
    length : float
         The length of the borehole    
    diameter : float
         The diameter of the borehole
         
    See Also
    ---------
    IntervalOrm : Relationship one to many with the IntervalOrm table.

    """
    __tablename__ = 'Boreholes'
    
    id = Column(String(32), primary_key=True)
    length = Column(Float(64), default=0.)
    diameter = Column(Float(64), default=0.)
    intervals = relationship('IntervalOrm', collection_class=attribute_mapped_collection('id'),
        cascade='all, delete-orphan')
    intervals_values = association_proxy('intervals', 'value',
                                         creator=lambda k, v:
                                         IntervalOrm(id=k, description=v['description'],
                                                     interval_number=v['interval_number'],
                                                     top=v['top'], base=v['base']))
    
    def __repr__(self):
        obj_class = str(self.__class__).strip('"<class>"').strip("' ")
        return f"<{obj_class}>(Name={self.id}, Length={self.length}, Diameter={self.diameter}, Intervals={len(self.intervals)})"


class PositionOrm(Base):
    """The Position table
    
    Attributes
    ----------
    id : int
        The id of the interval, different for each borehole interval.
    upper : float
           The upper value of the position.
    middle : float
            The middle value of the position.
    lower : float
           The lower value of the position.
    x : float
        The X coordinate.
    y : float
        The Y coordinate.
    z : float
        The Y coordinate, synonym of the middle attribute.    

    """
    __tablename__ = 'Positions'
    
    id = Column(Integer, primary_key=True)
    upper = Column(Float(32))
    middle = Column(Float(32))
    lower = Column(Float(32))
    x = Column(Float(64), default=0.)
    y = Column(Float(64), default=0.)
    z = synonym('middle')


class IntervalOrm(Base):
    """The Interval table
        
    Attributes
    ----------
    id : int
        The id of the interval, different for each borehole interval.
    borehole : str
        The name of the borehole from which the interval originated.
    interval_number : integer 
        The number the interval in the borehole, starts at 0 for the upper interval of each different borehole.
    description : str
        The name of the main component in the interval.
    top_id : int
        The id of the top position of the interval, link to the position id in the PositionOrm table.
    base_id : int
        The id of the base position of the interval, link to the position id in the PositionOrm table.
             
    See Also
    --------
    ComponentOrm : Relationship many to many with the Intervals table using the intermediate LinkIntervalComponentOrm table.
    PositionOrm : Relationship many to one with the Intervals table
    
    """
    __tablename__ = 'Intervals'
    
    id = Column(Integer, primary_key=True)
    borehole = Column(String(32), ForeignKey('Boreholes.id'))
    interval_number = Column(Integer)
    components = relationship('ComponentOrm', secondary='Linkintervalcomponent')
    description = Column(String(32))
    top_id = Column(Integer, ForeignKey('Positions.id'))
    top = relationship(PositionOrm, foreign_keys=[top_id])
    base_id = Column(Integer, ForeignKey('Positions.id'))
    base = relationship(PositionOrm, foreign_keys=[base_id])


class ComponentOrm(Base):
    """The Component table
    
    Attributes
    ----------
    id : str
        The id of the component.
    description : str
        The name of the component.
        
    See Also
    --------
    IntervalOrm : Relationship one to many with the IntervalOrm table.

    """
    __tablename__ = 'Components'
    
    id = Column(Integer, primary_key=True)
    intervals = relationship(IntervalOrm, secondary='Linkintervalcomponent')
    description = Column(String(32))

    def __repr__(self):
        obj_class = str(self.__class__).strip('"<class>"').strip("' ")
        return f"<{obj_class}>(Id={self.id}, Description={self.description}, Intervals={len(self.intervals)})"


class LinkIntervalComponentOrm(Base):
    """The junction table between component and interval
    
    Attributes
    ----------
    id : int
        The id of the interval, different for each borehole interval.
    description : str
                 The name of the component.
    
    """
    __tablename__ = 'Linkintervalcomponent'

    int_id = Column(Integer, ForeignKey('Intervals.id'), primary_key=True)
    comp_id = Column(Integer, ForeignKey('Components.id'), primary_key=True)
    extra_data = Column(String(256))
    component = relationship(ComponentOrm, backref=backref("component_assoc"))
    interval = relationship(IntervalOrm, backref=backref("interval_assoc"))


class SampleOrm(Base):
    """The Sample table

    Attributes
    ----------
    id : str
        The id of the sample.
    description : str
        The name of the sample.

    See Also
    --------
    IntervalOrm : Relationship one to many with the IntervalOrm table.

    """
    __tablename__ = 'Samples'

    id = Column(Integer, primary_key=True)
    type = Column(String(10))
    intervals = relationship(IntervalOrm, secondary='Linkintervalcomponent')
    description = Column(String(32))

    def __repr__(self):
        obj_class = str(self.__class__).strip('"<class>"').strip("' ")
        return f"<{obj_class}>(Id={self.id}, Description={self.description}, Intervals={len(self.intervals)})"


class PollutantOrm(Base):
    """The Pollutant table

    Attributes
    ----------
    id : str
        The id of the pollutant.
    description : str
        The name of the pollutant.

    See Also
    --------
    IntervalOrm : Relationship one to many with the IntervalOrm table.

    """
    __tablename__ = 'Pollutants'

    id = Column(String(32), primary_key=True)
    Family = Column(String(32))
    Concentration = Column(Float(64), default=0.)
    samples = relationship(SampleOrm, collection_class=attribute_mapped_collection('id'), cascade='all, delete-orphan')

    intervals = relationship(IntervalOrm, secondary='Linksamplepollutant')
    description = Column(String(32))

    def __repr__(self):
        obj_class = str(self.__class__).strip('"<class>"').strip("' ")
        return f"<{obj_class}>(Id={self.id}, Description={self.description}, Intervals={len(self.intervals)})"


class LinkSamplePollutantOrm(Base):
    """The junction table between component and interval

    Attributes
    ----------
    id : int
        The id of the interval, different for each borehole interval.
    description : str
        The name of the component.

    """

    __tablename__ = 'Linksamplepollutant'

    int_id = Column(Integer, ForeignKey('Samples.id'), primary_key=True)
    pol_id = Column(Integer, ForeignKey('Pollutants.id'), primary_key=True)
    extra_data = Column(String(256))
    pollutant = relationship(PollutantOrm, backref=backref("pollutant_assoc"))
    sample = relationship(SampleOrm, backref=backref("sample_assoc"))