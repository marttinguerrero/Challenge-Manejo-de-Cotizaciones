import json
import random
import time
import logging
from typing import Dict

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def simulacion_de_datos(source: str) -> str:
    companies = ["BMA", "GGAL", "YPF", "PAMP"]
    data = {
        "name": random.choice(companies),
        "buy": round(random.uniform(100, 200), 2),
        "sell": round(random.uniform(100, 200), 2),
        "timestamp": int(time.time() * 1000),
        "source": source,
    }
    return json.dumps(data)

class ManejoCotizaciones:
    def __init__(self):
        self.data: Dict[str, Dict[str, Dict[str, float]]] = {}

    def validar_datos(self, quote: dict) -> bool:
        """Valida que la cotización recibida tenga todos los campos necesarios y valores válidos."""
        required_keys = {"name", "buy", "sell", "timestamp", "source"}
        if not required_keys.issubset(quote.keys()):
            logging.error(f"Faltan campos en la cotización: {quote}")
            return False
        if not isinstance(quote["name"], str) or not isinstance(quote["source"], str):
            logging.error(f"Campos 'name' o 'source' inválidos en la cotización: {quote}")
            return False
        if not isinstance(quote["buy"], (int, float)) or not isinstance(quote["sell"], (int, float)):
            logging.error(f"Campos 'buy' o 'sell' inválidos en la cotización: {quote}")
            return False
        if not isinstance(quote["timestamp"], int):
            logging.error(f"Campo 'timestamp' inválido en la cotización: {quote}")
            return False
        return True

    def actualizar_datos(self, quote: dict):
        """Actualiza los datos almacenados con la última cotización válida."""
        company = quote["name"]
        source = quote["source"]
        if company not in self.data:
            self.data[company] = {}
        self.data[company][source] = {
            "buy": quote["buy"],
            "sell": quote["sell"],
            "timestamp": quote["timestamp"],
        }
        logging.info(f"Cotización actualizada: {company} desde {source}")

    def imprimir_cotizaciones(self):
        """Imprime las últimas cotizaciones almacenadas."""
        print("\nÚltimas cotizaciones:")
        for company, sources in self.data.items():
            print(f"Empresa: {company}")
            for source, quote in sources.items():
                print(f"  Fuente: {source}, Buy: {quote['buy']}, Sell: {quote['sell']}, Timestamp: {quote['timestamp']}")
        print()

def main():
    manager = ManejoCotizaciones()

    try:
        #ciclo continuo, apretar ctrl+c para detener el programa
        while True:
            for source in ["A", "B"]:
                raw_data = simulacion_de_datos(source)
                logging.info(f"Datos recibidos: {raw_data}")

                try:
                    quote = json.loads(raw_data)
                    if manager.validar_datos(quote):
                        manager.actualizar_datos(quote)
                        manager.imprimir_cotizaciones()
                except json.JSONDecodeError as e:
                    logging.error(f"Error al decodificar JSON: {e}")

            time.sleep(3)

    except KeyboardInterrupt:
        logging.info("Script detenido por el usuario.")

if __name__ == "__main__":
    main()
