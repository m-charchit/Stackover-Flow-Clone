from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

# For custom error pages
@errors.app_errorhandler(404) # Specficy what error to handle
def error_404(error):
    
    return render_template('404.html'), 404


@errors.app_errorhandler(403) 
def error_403(error):
    
    return render_template('403.html'), 403

@errors.app_errorhandler(405) 
def error_403(error):
    
    return render_template('405.html'), 405


@errors.app_errorhandler(500)
def error_500(error):
    
    return render_template('500.html'), 500