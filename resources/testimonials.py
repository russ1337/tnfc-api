from flask import Response, request, jsonify
from database.models import Testimonials, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, TestimonialNotExistsError, \
DeletingTestimonialError, FolderAlreadyExistsError, UpdatingTestimonialError


class TestimonialsApi(Resource):
    def get(self):
        pages = Testimonials.objects().to_json()
        return Response(pages, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            testimony =  Testimonials(**body)
            testimony.save()
            id = testimony.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise FolderAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class TestimonyApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            Testimonials.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise TestimonialNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            testimony = Testimonials.objects.get(id=id)
            testimony.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingTestimonialError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            testimony = Testimonials.objects.get(id=id).to_json()
            return Response(testimony, mimetype="application/json", status=200)
        except DoesNotExist:
            raise TestimonialNotExistsError
        except Exception:
            raise InternalServerError
