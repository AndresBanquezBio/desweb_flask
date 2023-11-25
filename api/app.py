from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)

    from modules.medics import bp as bpmedics
    from modules.patients import bp as bppatients
 
    app.register_blueprint(bpmedics)
    app.register_blueprint(bppatients) 

    return app
