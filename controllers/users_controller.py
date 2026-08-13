import json
import os

from flask import request, jsonify


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.json"
)


def carregar_usuarios():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_usuarios(usuarios):
    with open(DATA_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(
            usuarios,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


usuarios = carregar_usuarios()


def gerar_novo_id():
    if not usuarios:
        return 1

    return max(usuario["id"] for usuario in usuarios) + 1


def listar_usuarios():
    return jsonify({
        "data": usuarios
    }), 200


def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Nenhum dado foi enviado na requisicao."
        }), 400

    if not dados.get("nome"):
        return jsonify({
            "error": "O campo nome e obrigatorio."
        }), 400

    if not dados.get("email"):
        return jsonify({
            "error": "O campo email e obrigatorio."
        }), 400

    novo_usuario = {
        "id": gerar_novo_id(),
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    return jsonify({
        "data": novo_usuario
    }), 201


def buscar_usuario(id):
    usuario = next(
        (
            usuario
            for usuario in usuarios
            if usuario["id"] == id
        ),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuario nao encontrado."
        }), 404

    return jsonify({
        "data": usuario
    }), 200


def atualizar_usuario(id):
    usuario = next(
        (
            usuario
            for usuario in usuarios
            if usuario["id"] == id
        ),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuario nao encontrado."
        }), 404

    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Nenhum dado foi enviado para atualizacao."
        }), 400

    if not dados.get("nome"):
        return jsonify({
            "error": "O campo nome e obrigatorio."
        }), 400

    if not dados.get("email"):
        return jsonify({
            "error": "O campo email e obrigatorio."
        }), 400

    usuario["nome"] = dados["nome"]
    usuario["email"] = dados["email"]

    salvar_usuarios(usuarios)

    return jsonify({
        "data": usuario
    }), 200


def remover_usuario(id):
    usuario = next(
        (
            usuario
            for usuario in usuarios
            if usuario["id"] == id
        ),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuario nao encontrado."
        }), 404

    usuarios.remove(usuario)
    salvar_usuarios(usuarios)

    return "", 204
