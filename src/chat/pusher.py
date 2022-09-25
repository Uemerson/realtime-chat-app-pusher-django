import os
import pusher
from dotenv import load_dotenv

load_dotenv()

pusher_client = pusher.Pusher(
    app_id=os.getenv("app_id"),
    key=os.getenv("key"),
    secret=os.getenv("secret"),
    cluster=os.getenv("cluster"),
    ssl=True,
)
