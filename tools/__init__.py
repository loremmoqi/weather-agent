# use dict regist tools
from .weather_tool import get_weather
from .tool_schema import tools_schema
# 🌟 工具注册表：把工具名和真实的 Python 函数映射起来
# 以后新增工具，只需在这里加一行，Agent 核心代码一行都不用改！
TOOL_REGISTRY = {
    "get_weather":get_weather,
    # "search_web": search_web,      # 未来加搜索工具
    # "send_email": send_email,      # 未来加发邮件工具
}