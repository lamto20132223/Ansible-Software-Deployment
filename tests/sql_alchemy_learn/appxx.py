from flask import Flask 
from flask_restplus import Api, Resource, fields

import os

app = Flask(__name__)
api = Api(app)

a_language = api.model('Docker', {'file' : fields.String('file_name')})

languages = []
python = {'language' : 'Python'}
languages.append(python)

@api.route('/language')
class Language(Resource):
    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        os.system('bash /home/tupt18/upload_image.sh ' + str(api.payload['file']) )
        #languages.append(api.payload)
        return {'result' : 'ok added ' + str(api.payload['file'])}, 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9876)


# curl -X POST "http://172.16.29.193:9876/language" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"file\": \"docker.io/istio/pilot:1.4.4\"}"
