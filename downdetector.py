import httpx
import os
from utils.logs import logger_instance

class Downdetector:
    def __init__(self, url=None, nome_da_empresa=None):
        self.url = url
        self.nome_da_empresa = nome_da_empresa
        self.status_code = None
        self.resposta_corpo = None
    def get_api_url(self):
        return os.getenv(self.url, "https://downdetectorapi.com/v2/ping")
    async def fetch_data(self, url):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                response.raise_for_status() 
                return response.json()
            except httpx.HTTPStatusError as e:
                logger_instance.error(f"Erro na requisição: {e.response.status_code} - {e.response.text}")
                return None
            except Exception as e:
                logger_instance.exception("Erro inesperado ao buscar dados.")
                return None
    async def get_downdetector_data(self):
        url = self.get_api_url()
        data = await self.fetch_data(url)
        return data
