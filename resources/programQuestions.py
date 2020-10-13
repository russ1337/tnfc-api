from flask import Response, request
from flask_jwt_extended import create_access_token
from database.models import ProgramQuestions
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError

class ProgramQuestionsApi(Resource):
    def get(self):
        questions = ProgramQuestions.objects().to_json()
        return Response(questions, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            questions =  ProgramQuestions(**body)
            questions.save()
            id = questions.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError
