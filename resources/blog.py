from flask import Response, request, jsonify
from database.models import BlogPost, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, PostAlreadyExistsError, InternalServerError, \
UpdatingPostError, DeletingPostError, PostNotExistsError


class BlogPostsApi(Resource):
    def get(self):
        page = int(request.args.get('page'))
        perPage = int(request.args.get('per_page'))
        blogPosts = BlogPost.objects.order_by('-date_created_order').paginate(page=page, per_page=perPage)
        blogPosts.items.append({'totalPages': blogPosts.pages})
        blogPosts.items.append({'currentPage': blogPosts.page})
        blogPosts_Items = jsonify(blogPosts.items)
        return blogPosts_Items

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            blogPost =  BlogPost(**body, added_by=user)
            blogPost.save()
            id = blogPost.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise PostAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class BlogApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            BlogPost.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingPostError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            blogPost = BlogPost.objects.get(id=id)
            blogPost.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingPostError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            blogPosts = BlogPost.objects.get(id=id).to_json()
            return Response(blogPosts, mimetype="application/json", status=200)
        except DoesNotExist:
            raise PostNotExistsError
        except Exception:
            raise InternalServerError
