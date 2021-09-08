from common.logger import set_logger

logger = set_logger()


def main():
    logger.info("============infoメッセージ============")
    logger.warning("============warningメッセージ============")
    logger.error("============errorメッセージ============")


if __name__ == "__main__":
    main()
