# Import flask dependencies
from flask import Blueprint

# Define the blueprint: 'auth', set its url prefix: app.url/auth
transactions_blueprint = Blueprint('transactions', __name__)


# Set the route and accepted methods
@transactions_blueprint.route('/transactions', methods=['GET'])
def index():
    return 'Hello There!'
