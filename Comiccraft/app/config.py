from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    demo_mode: bool = True

    gemini_outline_model: str = "gemini-2.5-flash"
    gemini_story_model: str = "gemini-2.5-pro"

    hf_image_model: str = "black-forest-labs/FLUX.1-schnell"
    hf_provider: str = "auto"

    image_width: int = 768
    image_height: int = 768

    panels_dir: Path = Path("static/panels")
    exports_dir: Path = Path("static/exports")
    static_dir: Path = Path("static")
    templates_dir: Path = Path("templates")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()