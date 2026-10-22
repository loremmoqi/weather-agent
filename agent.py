# agent.py
import os
import json
from openai import OpenAI
from config import LLM_CONFIG
from tools import tools_schema, TOOL_REGISTRY  # 导入工具和注册表

# 初始化大模型客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=LLM_CONFIG["base_url"]
)
# 循环
def run_agent_turn(messages: list) -> str:
    """执行一次 Agent 循环（感知-决策-行动-观察）"""
    while True:
        response = client.chat.completions.create(
            model=LLM_CONFIG["model_name"],
            messages=messages,
            tools=tools_schema,
        )
        msg = response.choices[0].message

        # 如果 AI 决定直接回答，结束循环
        if not msg.tool_calls:
            messages.append(msg)
            return msg.content

        # 如果 AI 决定调用工具
        messages.append(msg)
        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)
            print(f"🔧 [Agent] 调用工具: {func_name}({func_args})")

            # 🌟 核心解耦：通过注册表动态调用工具，告别 if-else！
            if func_name in TOOL_REGISTRY:
                result = TOOL_REGISTRY[func_name](**func_args)
            else:
                result = {"error": f"未知工具: {func_name}"}

            # 将工具结果喂回给大模型
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result, ensure_ascii=False),
            })