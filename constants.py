"""AstrBot 万象画卷插件常量。"""

# API 超时配置
API_TIMEOUT_DEFAULT = 60.0
API_TIMEOUT_SLOW = 120.0
MAX_IMAGE_BYTES = 20 * 1024 * 1024
DEFAULT_BATCH_LIMIT = 10

class APIType:
    """接口类型枚举"""
    OPENAI_IMAGE = "openai_image"
    OPENAI_CHAT = "openai_chat"  # 新增 Chat 解析出图类型

class MessageEmoji:
    """消息表情符号"""
    ERROR = "❌"
    SUCCESS = "✅"
    WARNING = "⚠️"
    INFO = "ℹ️"
    PAINTING = "🎨"
