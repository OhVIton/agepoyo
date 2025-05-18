from enum import Enum


class LlmModel(Enum):
    """利用するLLMモデル種別."""

    GPT_41 = 1
    GPT_4O = 2

    GEMINI_20_FLASH = 20

    CLAUDE_37_SONNET = 40
    # 必要に応じて他モデルを追加
