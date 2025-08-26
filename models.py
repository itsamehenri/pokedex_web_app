from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemon"
    pokemon_id = Column(Integer, primary_key=True)
    pokemon_entry = Column(Integer)
    pokemon_name = Column(String)
    pokemon_type1 = Column(Integer, ForeignKey('types_id.id'))
    pokemon_type2 = Column(Integer, ForeignKey('types_id.id'))
    pokemon_generation = Column(Integer, ForeignKey('generations.id'))
    # Establish relationships for easier querying
    # type1 = relationship("Type", foreign_keys=[pokemon_type1], backref="pokemon_type1")
    # type2 = relationship("Type", foreign_keys=[pokemon_type2], backref="pokemon_type2")

class Type(Base):
    __tablename__ = "pokemon_types"
    type_id = Column(Integer, primary_key=True)
    type_name = Column(String)

class Generation(Base):
    __tablename__ = "pokemon_generations"
    generation_id = Column(Integer, primary_key=True)
    generation_name = Column(String)

# Create the table in the database
# Base.metadata.create_all(engine)