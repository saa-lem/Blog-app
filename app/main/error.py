from flask import render_template
from .import main
from ..import db

@main.errorhandler(404)
def error_404(error):
    return render_template('/404.html'), 404


@main.errorhandler(403)
def error_403(error):
    return render_template('/403.html'), 403


@main.errorhandler(500)
def error_500(error):
    return render_template('/500.html'), 500