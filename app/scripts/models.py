from sentence_transformers import SentenceTransformer

from ..constants.types import TRANSFORMER_MODEL_NAME
from ..utils.fs import get_model_path

def download_model():
    model = SentenceTransformer(TRANSFORMER_MODEL_NAME)
    model.save(get_model_path())

if __name__ == "__main__":
    download_model()
    print(f"Model {TRANSFORMER_MODEL_NAME} downloaded and saved to {get_model_path()}")