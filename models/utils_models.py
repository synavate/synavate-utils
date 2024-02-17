from pydantic import BaseModel, Validation, Field
from typing import Dict, List, Union
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AppConfig:
    name: str
    version: str
    author: str
    description: str
    license: str

class SynavateUtils(BaseModel):
    name: str
    version: str
    author: str
    description: str
    license: str

    class Config:
        # Use dataclass field name for alias
        alias_generator = lambda field_name: field_name

def load_config_from_file(file_path: str) -> SynavateUtils:
    with open(file_path, "r") as file:
        config_data = file.read()

    try:
        config_model = SynavateUtils.parse_raw(config_data)
    except ValidationError as e:
        raise ValueError(f"Invalid configuration data: {e}")

    return config_model



if __name__ == "__main__":
    try:
        config = load_config_from_file("config.yaml")
        print("Loaded configuration:", config)
    except ValueError as e:
        print(e)


    