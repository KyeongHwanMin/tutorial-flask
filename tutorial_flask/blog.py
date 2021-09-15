from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from tutorial_flask.auth import login_required
from tutorial_flask.db import get_db

bp = Blueprint('blog', __name__)