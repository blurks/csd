from zope.interface import implementer
from sqlalchemy import (
    Column,
    String,
    Unicode,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property

from clld import interfaces
from clld.db.meta import Base, CustomModelMixin
from clld.db.models.common import Value, HasSourceMixin, Language, Parameter


#-----------------------------------------------------------------------------
# specialized common mapper classes
#-----------------------------------------------------------------------------
@implementer(interfaces.ILanguage)
class Languoid(Language, CustomModelMixin):
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)
    ord = Column(Integer)


@implementer(interfaces.IParameter)
class Entry(Parameter, CustomModelMixin):
    pk = Column(Integer, ForeignKey('parameter.pk'), primary_key=True)
    ps = Column(Unicode)
    sd = Column(Unicode)


@implementer(interfaces.IValue)
class Counterpart(Value, CustomModelMixin):
    pk = Column(Integer, ForeignKey('value.pk'), primary_key=True)
    cognate = Column(Unicode)
    comment = Column(Unicode)


class ValueReference(Base, HasSourceMixin):
    """
    """
    value_pk = Column(Integer, ForeignKey('value.pk'))
    value = relationship(Value, backref="references")