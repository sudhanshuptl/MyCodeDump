from flask import Flask, Blueprint
from flask_restplus import Api, Resource,  fields
from marshmallow import Schema, fields as ma_fields, post_load

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api') # default minimum url ex abc.com/api becomes base url
# doc='/documentation' move documentation to `/doc='/documentation'` path instead of home page
api = Api(blueprint, doc='/documentation')  # doc=False) to disable swagger UI
# New path for swagger UI : http://127.0.0.1:5000/api/documentation


app.register_blueprint(blueprint)  # register blueprint with app

app.config['SWAGGER_UI_JSONEDITOR'] = True  # enable json editor in swagger





# structure of language json
# 1st parameter is name of model `Language`
#language_model = api.model('Language',{'language_name': fields.String('The language')}) #restplus field


class Language(object):
    def __init__(self, language, framework):
        self.language = language
        self.framework = framework

    def __repr__(self):
        return '{} is language, {} is framework'.format(self.language, self.framework)


class LanguageSchema(Schema):
    language = ma_fields.String()
    framework = ma_fields.String()

    @post_load
    def create_language(self, data):
        return Language(**data)


languages = []
python = Language(language='Python',  framework='Flask')
languages.append(python)

@api.route('/language')
class Language(Resource):
    # it automatically filter out `id` from result as not specified in final model
    #@api.marshal_with(language_model, envelope='the_data') # envelop will add extra key in begining of final response
    def get(self):
        # to handle get request define this function

        my_schema = LanguageSchema(many=True) # many= True means expecting a list of object of this schema
        return my_schema.dump(languages)

    #@api.expect(language_model)
    def post(self):
        new_lang = api.payload
        new_lang['id'] = len(languages) + 1
        languages.append(new_lang)
        return {'msg': 'language Added '}, 201


if __name__ == '__main__':
    app.run(debug=True)
