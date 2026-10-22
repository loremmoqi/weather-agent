import os

# LLM config
# OPENAI_API_KEY已经在环境变量配置了sk-87a722acbe5a4a099490e66dd167c09a。
LLM_CONFIG = {
    "model_name" :os.getenv("MODEL_NAME","deepseek-chat"),
    "base_url":os.getenv("OPENAI_BASE_URL","https://api.deepseek.com/v1")
}

# third-party API config
AMAP_KEY = os.getenv("AMAP_KEY","b9b4b2c4a1177c8c66133bdea19ecf00")
