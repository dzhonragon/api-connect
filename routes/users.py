from flask import Blueprint

from controllers.users_controller import (
    listar_usuarios,
    cadastrar_usuario,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario
)

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_usuarios():
    return listar_usuarios()


@users_bp.route("/users", methods=["POST"])
def post_usuario():
    return cadastrar_usuario()


@users_bp.route("/users/<int:id>", methods=["GET"])
def get_usuario_por_id(id):
    return buscar_usuario(id)


@users_bp.route("/users/<int:id>", methods=["PUT"])
def put_usuario(id):
    return atualizar_usuario(id)


@users_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    return remover_usuario(id)
