from hatak.application import Application

from .routes import make_routes

main = Application('kasamoja', make_routes)
