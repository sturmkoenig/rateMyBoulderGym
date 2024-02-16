# coding=utf-8
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin


from .entities.entity import Session, engine, Base
from .entities.rating import Rating, RatingSchema

app = Flask(__name__)
CORS(app, resources={r"/rating*": {"origins": "*"}})
app.config['CORS_ALLOW_HEADERS'] = "Content-Type"
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

# generate database schema
Base.metadata.create_all(engine)

@app.route('/rating')
def get_ratings():
    session = Session()
    rating_objects = session.query(Rating).all()

    schema = RatingSchema(many = True)
    ratings = schema.dump(rating_objects)

    session.close()
    return jsonify(ratings)


@app.route('/rating', methods=['PUT'])
def put_rating():
    posted_rating = RatingSchema()\
        .load(request.get_json())
    
    print(posted_rating)
    rating = Rating(**posted_rating)

    session = Session()
    session.merge(rating)
    session.commit()

    new_rating = RatingSchema().dump(rating)
    session.close()
    return jsonify(new_rating), 201
