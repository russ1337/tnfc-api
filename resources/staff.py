from flask import Response, request
from database.models import Staff, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, StaffAlreadyExistsError, InternalServerError, \
UpdatingStaffError, DeletingStaffError, StaffNotExistsError
from PIL import Image
from io import BytesIO
import base64

class StaffsApi(Resource):
    def get(self):
        staffs = Staff.objects().to_json()
        return Response(staffs, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            decodedImage = base64.b64decode(body['photo'])
            del body['photo']
            staff =  Staff(**body, photo=decodedImage)
            staff.save()
            id = staff.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise StaffAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class StaffPicApi(Resource):
    def get(self, id):
        try:
            staff_pic = Staff.objects.get(id=id).staff_photo()
            return staff_pic
        except DoesNotExist:
            raise PostNotExistsError
        except Exception:
            raise InternalServerError

class StaffApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            if body['photo'] != '':
                decodedImage = base64.b64decode(body['photo'])
                Staff.objects.get(id=id).update(photo=decodedImage)
            del body['photo']
            Staff.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingStaffError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            staff = Staff.objects.get(id=id)
            staff.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingStaffError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            staffs = Staff.objects.get(id=id).to_json()
            return Response(staffs, mimetype="application/json", status=200)

        except DoesNotExist:
            raise StaffNotExistsError
        except Exception:
            raise InternalServerError
