# tools/tool_schema.py
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市指定日期的实时天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称，如 北京、桂林"},
                    "date": {"type": "string", "description": "日期，默认 today", "default": "today"}
                },
                "required": ["city"]
            }
        }
    }
]