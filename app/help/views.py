from flask import Blueprint, render_template
from flask.ext.security import login_required

from app import cache

blueprint = Blueprint('help', __name__)

@blueprint.route('/<command>/<type>/')
@cache.cached
def help_command(command, type):
    content = pages.get_or_404(command)
    
    return render_template('help_{0}.html'.format(type), content=content)