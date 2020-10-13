from .staff import StaffsApi, StaffApi, StaffPicApi
from .ftp import ListFiles, FileApi
from .auth import SignupApi, LoginApi
from .blog import BlogPostsApi, BlogApi
from .pages import PagesApi, PageApi
from .testimonials import TestimonialsApi, TestimonyApi
from .newsletterSignup import NewsletterSignupApi
from .programQuestions import ProgramQuestionsApi
from .messages import MessagesApi
from .volunteerSignup import VolunteerSignupApi

def initialize_routes(api):
    api.add_resource(StaffsApi, '/api/staff')
    api.add_resource(StaffApi, '/api/staff/<id>')
    api.add_resource(StaffPicApi, '/api/staff/pic/<id>')

    api.add_resource(PagesApi, '/api/pages')
    api.add_resource(PageApi, '/api/pages/<id>')

    api.add_resource(TestimonialsApi, '/api/testimonials')
    api.add_resource(TestimonyApi, '/api/testimonials/<id>')

    api.add_resource(ListFiles, '/api/file')
    api.add_resource(FileApi, '/api/files/<articleId>/<filename>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(NewsletterSignupApi, '/api/newsletter-signup')

    api.add_resource(VolunteerSignupApi, '/api/volunteer-signup')

    api.add_resource(ProgramQuestionsApi, '/api/program-questions')

    api.add_resource(MessagesApi, '/api/messages')

    api.add_resource(BlogPostsApi, '/api/blog/posts')
    api.add_resource(BlogApi, '/api/blog/<id>')
