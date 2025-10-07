from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432

    # Kafka
    KAFKA_BROKER: str
    KAFKA_TOPIC: str

    # gRPC
    VEHICLE_GRPC_HOST: str
    VEHICLE_GRPC_PORT: int

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()