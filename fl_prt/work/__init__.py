from flask import Blueprint

work = Blueprint('work', __name__, template_folder='templates')

from . import views

