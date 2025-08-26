from db import session
from models import Pokemon, Type, Generation
from sqlalchemy.orm import aliased
from sqlalchemy import and_

def get_all_types():
    # Retrive all types
    return session.query(Type).all()

def get_all_generations():
    # Retrieve all generations
    return session.query(Generation).all()

def get_all_pokemon(name, type1, type2, region):

    print(name, type1, type2, region)

    PokemonType1 = aliased(Type)
    PokemonType2 = aliased(Type)
    # Retrieve all pokemon
    query = session.query(
        Pokemon.pokemon_id.label("pokemon_id"),
        Pokemon.pokemon_entry.label("pokemon_entry"),
        Pokemon.pokemon_name.label("pokemon_name"), 
        PokemonType1.type_name.label("pokemon_type_1"),
        PokemonType2.type_name.label("pokemon_type_2"),
        Generation.generation_name.label("pokemon_generation")
        ).outerjoin(
            PokemonType1, Pokemon.pokemon_type1 == PokemonType1.type_id
        ).outerjoin(
            PokemonType2, Pokemon.pokemon_type2 == PokemonType2.type_id
        ).outerjoin(
            Generation, Pokemon.pokemon_generation == Generation.generation_id
        ).filter(Pokemon.pokemon_name.like(f'%{name}%'))
    
    if type1 != 0:
        query = query.filter(Pokemon.pokemon_type1 == type1)
    
    if type2 != 0:
        query = query.filter(Pokemon.pokemon_type2 == type2)
    
    if region != 0:
        query = query.filter(Pokemon.pokemon_generation == region)

    return query.all()

# print(get_all_pokemon("", 1, 0, 0))