

from efipay import EfiPay
import hmac
import hashlib
from flask.views import MethodView


URL_PROD = "https://pix.api.efipay.com.br"
CLIENT_ID = "Client_Id_22639387ce0399f7e466a446772bf46b60638623"
CLIENT_SECRET = "Client_Secret_747e55edfc66597c98e016cd00a828f037ed73c4"
CERTIFICADO = "src/certificates/certificadoEfi.pem"

CREDENTIALS = {
    'client_id': 'Client_Id_22639387ce0399f7e466a446772bf46b60638623',
    'client_secret': 'Client_Secret_747e55edfc66597c98e016cd00a828f037ed73c4',
    'sandbox': False,  # True: Ambiente de Homologação |  False: Ambiente de Produção
    'certificate': 'src/certificates/certificadoEfi.pem'
}


class CadastrarWebhook (MethodView):
    def get(self):
        efi = EfiPay(CREDENTIALS)

        headers = {
            'x-skip-mtls-checking': 'false'
        }

        params = {
            'chave': 'fe308151-0a14-49c1-acd6-6487adc8f08f'
        }

        url_webhook = 'https://modelo-flask.onrender.com/'
        secret_key = b'1234'

        hash_hmac = hmac.new(secret_key, url_webhook.encode(), hashlib.sha256).hexdigest()
        url_webhook_com_hash = f'{url_webhook}?hmac={hash_hmac}&ignorar='
        print(url_webhook_com_hash)
        body = {
            'webhookUrl': url_webhook_com_hash
        }

        response = efi.pix_config_webhook(params=params, body=body, headers=headers)
        print("passou no cadastrar web")
        return response
