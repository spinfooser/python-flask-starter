from flask import Flask, render_template
from app.transactions.controllers import transactions_blueprint as tx_module

app = Flask(__name__, instance_relative_config=True)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return 'not found'


# Register blueprint(s)
app.register_blueprint(tx_module)
