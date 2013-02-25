from flask import Blueprint, render_template
from flask.ext.security import login_required

blueprint = Blueprint('terminal', __name__)

@blueprint.route('/')
@login_required
def index():
    return render_template('terminal/index.html')