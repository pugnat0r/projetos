import mercadopago
import base64
from PIL import Image
from io import BytesIO
import time

ACCESS_TOKEN = "APP_USR-4935719068443239-032611-ace533cb5fc281b0a36f0bdcace7a8ee-672696771"

sdk = mercadopago.SDK(ACCESS_TOKEN)


def criar_pagamento(valor, descricao):
    payment_data = {
        "transaction_amount": valor,
        "description": descricao,
        "payment_method_id": "pix",
        "payer": {"email": "teste@test.com"}
    }

    payment = sdk.payment().create(payment_data)
    resposta = payment["response"]

    payment_id = resposta["id"]

    # gerar imagem do QR
    qr_base64 = resposta["point_of_interaction"]["transaction_data"]["qr_code_base64"]
    qr_bytes = base64.b64decode(qr_base64)
    image = Image.open(BytesIO(qr_bytes))
    image = image.resize((250, 250))

    return payment_id, image


def verificar_status(payment_id):
    status = sdk.payment().get(payment_id)
    return status["response"]["status"]
