from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download

# Will return the actual path where it's stored
path = snapshot_download("meta-llama/Llama-2-7B-Chat-hf")
print(path)