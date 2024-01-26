# -- coding: utf-8 --
# @Time : 2024/1/26 18:36
# @Author : JiahuaLInk
# @Email : 840132699@qq.com
# @File : skills.py
# @Software: PyCharm
from exts import db


class SkillsModel(db.Model):
    skill_id = db.Column(db.Integer, primary_key=True)
    chinese_name = db.Column(db.String(255))
    english_name = db.Column(db.String(255))
    type = db.Column(db.String(50))
    category = db.Column(db.String(50))
    power = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    pp = db.Column(db.Integer)
    faint = db.Column(db.Integer)
    poison = db.Column(db.Integer)
    burn = db.Column(db.Integer)
    paralyze = db.Column(db.Integer)
    sleep = db.Column(db.Integer)
    freeze = db.Column(db.Integer)
    flinch = db.Column(db.Integer)
    confuse = db.Column(db.Integer)
    attract = db.Column(db.Integer)
    charge = db.Column(db.Integer)
    bind = db.Column(db.Integer)
    recoil = db.Column(db.Integer)
    rigid = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    special_attack = db.Column(db.Integer)
    special_defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    hit_rate = db.Column(db.Integer)
    evasion = db.Column(db.Integer)

    @classmethod
    def create_skill(cls, chinese_name, english_name, type, category, power, accuracy, pp, faint, poison, burn,
                     paralyze, sleep, freeze, flinch, confuse, attract, charge, bind, recoil, rigid, attack, defense,
                     special_attack, special_defense, speed, hit_rate, evasion, english_effect):
        new_skill = cls(chinese_name=chinese_name, english_name=english_name, type=type, category=category,
                        power=power, accuracy=accuracy, pp=pp, faint=faint, poison=poison, burn=burn, paralyze=paralyze,
                        sleep=sleep, freeze=freeze, flinch=flinch, confuse=confuse, attract=attract, charge=charge,
                        bind=bind, recoil=recoil, rigid=rigid, attack=attack, defense=defense,
                        special_attack=special_attack, special_defense=special_defense, speed=speed,
                        hit_rate=hit_rate, evasion=evasion, english_effect=english_effect)
        db.session.add(new_skill)
        db.session.commit()
        return new_skill

    @classmethod
    def get_all_skills(cls):
        return cls.query.all()

    @classmethod
    def get_skill_by_id(cls, skill_id):
        return cls.query.get(skill_id)

    def update_skill(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete_skill(self):
        db.session.delete(self)
        db.session.commit()