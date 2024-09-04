from src.controllers.index import index

routes = {
    "index_route": "/", "index_controller": index.as_view("index"),
}
