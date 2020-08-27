from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path,encoding="utf-8_sig")

setting_url = os.environ["DATABASE_URL"]
secret_key = os.environ["SECRET_KEY"]