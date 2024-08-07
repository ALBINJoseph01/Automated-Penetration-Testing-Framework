import logging
import yaml

def setup_logger():
    with open("config/settings.yaml", 'r') as f:
        config = yaml.safe_load(f)

    logging.basicConfig(
        filename="framework.log",
        level=config['logging_level'],
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)