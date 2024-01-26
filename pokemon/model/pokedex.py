# -- coding: utf-8 --
# @Time : 2024/1/26 18:35
# @Author : JiahuaLInk
# @Email : 840132699@qq.com
# @File : pokedex.py
# @Software: PyCharm
from exts import db


class PokedexModel(db.Model):
    poke_id = db.Column(db.Integer, primary_key=True)
    chinese_name = db.Column(db.String(255))
    english_name = db.Column(db.String(255))
    type1 = db.Column(db.String(50))
    type2 = db.Column(db.String(50))
    ability1 = db.Column(db.String(50))
    ability2 = db.Column(db.String(50))
    hidden_ability = db.Column(db.String(50))
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    special_attack = db.Column(db.Integer)
    special_defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)

    @classmethod
    def get_all_pokemons(cls):
        return cls.query.all()

    @classmethod
    def get_pokemon_by_id(cls, pokemon_id):
        return cls.query.get(pokemon_id)

    @classmethod
    def get_pokemons_by_type(cls, pokemon_type):
        return cls.query.filter((cls.type1 == pokemon_type) | (cls.type2 == pokemon_type)).all()

    def update_pokemon(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete_pokemon(self):
        db.session.delete(self)
        db.session.commit()
