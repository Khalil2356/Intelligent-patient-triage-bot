from huggingface_hub import snapshot_download
from pathlib import Path

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
local_dir = Path.cwd() / "models" / "TinyLlama-1.1B-Chat-v1.0"
local_dir.mkdir(parents=True, exist_ok=True)

snapshot_download(
    repo_id=model_id,
    allow_patterns=["*.safetensors", "*.json", "tokenizer.model*"],
    local_dir=local_dir,
    local_dir_use_symlinks=False
)

print(f"Model downloaded to: {local_dir}")