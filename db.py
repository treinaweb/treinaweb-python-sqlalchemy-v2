from sqlalchemy import create_engine

from config import config


engine = create_engine(
    f"mysql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
)
