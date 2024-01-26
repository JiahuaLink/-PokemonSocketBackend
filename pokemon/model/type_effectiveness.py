# -- coding: utf-8 --
# @Time : 2024/1/26 18:38
# @Author : JiahuaLInk
# @Email : 840132699@qq.com
# @File : type_effectiveness.py
# @Software: PyCharm
from exts import db


class TypeEffectivenessModel(db.Model):
    attacking_type = db.Column(db.String(50), primary_key=True)
    normal = db.Column(db.Float)
    fighting = db.Column(db.Float)
    flying = db.Column(db.Float)
    poison = db.Column(db.Float)
    ground = db.Column(db.Float)
    rock = db.Column(db.Float)
    bug = db.Column(db.Float)
    ghost = db.Column(db.Float)
    steel = db.Column(db.Float)
    fire = db.Column(db.Float)
    water = db.Column(db.Float)
    grass = db.Column(db.Float)
    electric = db.Column(db.Float)
    psychic = db.Column(db.Float)
    ice = db.Column(db.Float)
    dragon = db.Column(db.Float)
    dark = db.Column(db.Float)
    fairy = db.Column(db.Float)

    @classmethod
    def create_type_effectiveness(cls, attacking_type, normal, fighting, flying, poison, ground, rock, bug, ghost,
                                  steel, fire, water, grass, electric, psychic, ice, dragon, dark, fairy):
        new_type_effectiveness = cls(attacking_type=attacking_type, normal=normal, fighting=fighting, flying=flying,
                                     poison=poison, ground=ground, rock=rock, bug=bug, ghost=ghost, steel=steel,
                                     fire=fire, water=water, grass=grass, electric=electric, psychic=psychic, ice=ice,
                                     dragon=dragon, dark=dark, fairy=fairy)
        db.session.add(new_type_effectiveness)
        db.session.commit()
        return new_type_effectiveness

    @classmethod
    def get_all_type_effectiveness(cls):
        return cls.query.all()

    @classmethod
    def get_type_effectiveness_by_attacking_type(cls, attacking_type):
        return cls.query.filter(cls.attacking_type == attacking_type).first()

    def update_type_effectiveness(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete_type_effectiveness(self):
        db.session.delete(self)
        db.session.commit()