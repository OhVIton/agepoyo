from enum import Enum


class LlmModel(Enum):
    """利用するLLMモデル種別."""

    GPT_41 = 1

    GEMINI_20_FLASH = 20
    # 必要に応じて他モデルを追加
