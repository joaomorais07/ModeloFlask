from flask.views import MethodView


class index (MethodView):
        def get(self):
                return 200
