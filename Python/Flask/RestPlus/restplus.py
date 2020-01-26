from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api') # default minimum url ex abc.com/api becomes base url
# doc='/documentation' move documentation to `/doc='/documentation'` path instead of home page
api = Api(blueprint, doc='/documentation')  # doc=False) to disable swagger UI
# New path for swagger UI : http://127.0.0.1:5000/api/documentation


app.register_blueprint(blueprint)  # register blueprint with app

app.config['SWAGGER_UI_JSONEDITOR'] = True  # enable json editor in swagger




languages = [{'language_name': 'Python', 'id': 1}]

# structure of language json
# 1st parameter is name of model `Language`
language_model = api.model('Language',{'language_name': fields.String('The language')})


@api.route('/language')
class Language(Resource):
    # it automatically filter out `id` from result as not specified in final model
    @api.marshal_with(language_model, envelope='the_data') # envelop will add extra key in begining of final response
    def get(self):
        # to handle get request define this function
        return languages

    @api.expect(language_model)
    def post(self):
        new_lang = api.payload
        new_lang['id'] = len(languages) + 1
        languages.append(new_lang)
        return {'msg': 'language Added '}, 201


if __name__ == '__main__':
    app.run(debug=True)
