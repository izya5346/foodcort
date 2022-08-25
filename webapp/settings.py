from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_host: str
    app_port: str
    redis_host: str
    redis_port: str
    ngrok_token: str
    ngrok_region: str
    public_url: str = ''    

    def get_db(cls):
        return f"{cls.db_engine}://{cls.db_username}:{cls.db_password}@{cls.db_name}.{cls.db_host}:{cls.db_port}"

    def get_redis(cls):
        return f"redis://{cls.redis_host}:{cls.redis_port}"

    def get_app(cls):
        return f"http://{cls.app_host}:{cls.app_port}"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
