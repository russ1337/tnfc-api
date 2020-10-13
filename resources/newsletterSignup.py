from flask import Response, request
from flask_jwt_extended import create_access_token
from database.models import Messages
from flask_restful import Resource
import datetime
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError

class NewsletterSignupApi(Resource):
    def get(self):
        questions = Messages.objects().to_json()
        return Response(questions, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            email =  Messages(**body)
            email.save()
            id = email.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError
