import os
import openai
from dotenv import load_dotenv, find_dotenv
from typing import List, Union, Tuple, Dict

load_dotenv(find_dotenv())
mlops_cred: Dict = {}

list_mlops = []


#List of configs
mlops_cred["openai_api_key"] = os.getenv("OPENAI_API_KEY")

    
    
