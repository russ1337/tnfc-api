from flask import Response, request, jsonify
from database.models import Pages, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, PostAlreadyExistsError, InternalServerError, \
DeletingPostError, PostNotExistsError


class PagesApi(Resource):
    def get(self):
        pages = Pages.objects().to_json()
        return Response(pages, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            page =  Pages(**body)
            page.save()
            id = page.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise PostAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class PageApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            Pages.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingPostError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            page = Pages.objects.get(id=id).to_json()
            return Response(page, mimetype="application/json", status=200)
        except DoesNotExist:
            raise PostNotExistsError
        except Exception:
            raise InternalServerError
