import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1978415696,
]

KYNAN = list(map(int, os.getenv("KYNAN", "1978415696").split()))

API_ID = int(os.getenv("API_ID", "17250424"))

API_HASH = os.getenv("API_HASH", "753bc98074d420ef57ddf7eb1513162b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6715085237:AAG_e-Wz-4Ch4YqkNgVF5YGm2xe69NlrQeI")

OWNER_ID = int(os.getenv("OWNER_ID", "1978415696"))

USER_ID = list(map(int, os.getenv("USER_ID", "1978415696").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002122323679"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002073424041"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001473548283").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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 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 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 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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://vewonon211:vewonon211@joysoy.kokbtub.mongodb.net/?retryWrites=true&w=majority",
)
