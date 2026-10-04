from src.config import settings
from loguru import logger

def main():
    logger.info("=== 1. HAFTA 1. ADIM KONTROLU ===")
    logger.info(f"Uygulama Adi: {settings.APP_NAME}")
    logger.info(f"Debug Modu: {settings.DEBUG}")
    logger.info(f"User-Agent: {settings.USER_AGENT[:50]}...")
    logger.info(f"Request Timeout: {settings.REQUEST_TIMEOUT}s")
    logger.success("Proje yapisi ve konfigurasyon basariyla dogrulandi!")

if __name__ == "__main__":
    main()
