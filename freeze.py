from flask_frozen import Freezer

from app import app
from config import cfg

app.config["FREEZER_DESTINATION"] = "docs"

freezer = Freezer(app)

@freezer.register_generator
def conference():
    for name in cfg.keys():
        yield {"conference": name}

if __name__ == "__main__":
    freezer.freeze()