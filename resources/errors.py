class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class StaffAlreadyExistsError(Exception):
    pass


class UpdatingStaffError(Exception):
    pass


class DeletingStaffError(Exception):
    pass


class StaffNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class PostAlreadyExistsError(Exception):
    pass


class UpdatingPostError(Exception):
    pass


class DeletingPostError(Exception):
    pass


class PostNotExistsError(Exception):
    pass


class FolderAlreadyExistsError(Exception):
    pass


class TestimonialNotExistsError(Exception):
    pass


class DeletingTestimonialError(Exception):
    pass


class UpdatingTestimonialError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "FolderAlreadyExistsError": {
        "message": "A folder with that ID already exists. Try refreshing the page.",
        "status": 400
    },
    "TestimonialNotExistsError": {
        "message": "Testimonial Does Not Exist",
        "status": 400
    },
    "DeletingTestimonialError": {
        "message": "Deleting Testimonial Failed",
        "status": 400
    },
    "UpdatingTestimonialError": {
        "message": "Testimonial Update Failed",
        "status": 400
    },
    "PostAlreadyExistsError": {
        "message": "Post with given title already exists",
        "status": 400
    },
    "UpdatingPostError": {
        "message": "Updating post added by other is forbidden",
        "status": 403
    },
    "DeletingPostError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403
    },
    "PostNotExistsError": {
        "message": "Movie with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "StaffAlreadyExistsError": {
        "message": "Staff with given name already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
