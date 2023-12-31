from huggingface_hub import snapshot_download, move_repo
from os import environ

MODEL = environ.get("BASE_MODEL_REPO_ID")

snapshot_download(
  MODEL,
  revision="main",
  local_dir="/outputs/model",
  local_dir_use_symlinks=False,
)

move_repo()
