from flask import Blueprint

from . import views

web_routes = Blueprint('web', __name__)


web_routes.add_url_rule('/', 'home', views.Home.as_view('home'))
web_routes.add_url_rule('/user/', 'user_create', views.UserDetailView.as_view('user_create'), methods=['POST'])
web_routes.add_url_rule('/user/<int:id>/', 'user_detail', views.UserDetailView.as_view('user_detail'), methods=['GET'])
web_routes.add_url_rule('/users/', 'user_list', views.UsersListView.as_view('user_list'))
web_routes.add_url_rule('/<string:name>/', 'greet', views.Greet.as_view('greet'))
