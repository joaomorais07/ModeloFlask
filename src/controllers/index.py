from flask.views import MethodView
from flask import render_template

class index (MethodView):
        def get(self):
                return render_template("principal.html")
