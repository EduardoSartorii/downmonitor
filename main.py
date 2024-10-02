import asyncio
from downdetector import Downdetector
from utils.logs import logger_instance

async def main():
    downdetector = Downdetector()
    data = await downdetector.get_downdetector_data()
    if data:
        logger_instance.info("Dados coletados com sucesso:")
        print(data)
    else:
        print("Nenhum dado foi coletado.")

if __name__ == "__main__":
    asyncio.run(main())  # Executa a função principal
