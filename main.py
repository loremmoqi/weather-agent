# main.py
from agent import run_agent_turn
# import os

def main():
    messages = [
        {"role": "system", "content": "你是一个全能助手，擅长使用工具解决用户问题。用自然语言回答。"},
    ]
    print("🤖 高级 Agent 已启动，输入 'quit' 退出\n")

    while True:
        user_input = input("👤 ")
        if user_input.lower() in ["quit", "exit", "退出"]:
            print("👋 再见！")
            break
            
        messages.append({"role": "user", "content": user_input})
        
        # 调用 Agent 核心逻辑
        reply = run_agent_turn(messages)
        print(f"🤖 {reply}\n")

if __name__ == "__main__":
    main()