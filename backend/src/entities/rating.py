from sqlalchemy import Column, String, Integer, Float
from marshmallow import Schema, fields

from .entity import Base


class Rating(Base):
    __tablename__ = 'ratings'

    boulder_gym_name = Column(String, primary_key=True)
    user_name = Column(String, primary_key=True)
    rating_fun = Column(Float)
    rating_training_area = Column(Float)
    rating_music = Column(Float)
    rating_food = Column(Float)
    rating_coffe = Column(Float)
    rating_athmosphere = Column(Float)
    rating_shop = Column(Float)
    rating_child_pollution = Column(Float)

    def __init__(self, 
                 boulder_gym_name,
                 user_name,
                 rating_fun, 
                 rating_training_area, 
                 rating_music, 
                 rating_food, 
                 rating_coffe, 
                 rating_athmosphere, 
                 rating_shop, 
                 rating_child_pollution,
                ):
        self.boulder_gym_name = boulder_gym_name
        self.user_name = user_name
        self.rating_fun = rating_fun
        self.rating_training_area = rating_training_area
        self.rating_music = rating_music
        self.rating_food = rating_food
        self.rating_coffe = rating_coffe
        self.rating_athmosphere = rating_athmosphere
        self.rating_shop = rating_shop
        self.rating_child_pollution = rating_child_pollution

class RatingSchema(Schema):
    id = fields.Number()
    user_name = fields.Str()
    boulder_gym_name = fields.Str()
    rating_fun = fields.Number()
    rating_training_area = fields.Number()
    rating_music = fields.Number()
    rating_food = fields.Number()
    rating_coffe = fields.Number()
    rating_athmosphere = fields.Number()
    rating_shop = fields.Number()
    rating_child_pollution = fields.Number()

