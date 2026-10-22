# 🌤️ AI Weather Agent

一个基于大语言模型（LLM）和工具调用（Tool Calling）技术的多轮对话天气查询助手。该项目采用模块化工程架构，展示了 AI Agent "感知-决策-行动-观察" 的核心闭环。

## ✨ 核心特性

- **多轮对话记忆**：支持上下文连续对话，可基于历史信息进行对比分析（如“这两个城市哪个更热？”）。
- **真实世界数据接入**：通过集成高德地图 API，获取精准的实时天气数据，彻底告别大模型幻觉。
- **模块化工程架构**：核心逻辑、工具实现、配置文件完全解耦，支持通过 `TOOL_REGISTRY` 零代码修改无缝扩展新工具。
- **安全配置管理**：使用 `.env` 文件管理敏感 API Key，配合 `.gitignore` 确保密钥绝不泄露。

## 🏗️ 项目结构


1. 安装requirements.txt中的包
2. 在环境变量导入你的LLM的API，比如在conda中：
` conda env config vars set OPENAI_API_KEY="sk-你的真实密钥填在这里"`
`conda env config vars set OPENAI_BASE_URL="https://api.deepseek.com/v1"`
3. 按照下面的结构写内容
weather_agent_pro/
├── main.py                 # 1. 程序入口：负责终端交互（多轮对话）
├── config.py               # 2. 配置文件：集中管理 API Key、模型名称等
├── agent.py                # 3. Agent 核心：纯粹的“感知-决策-行动-观察”循环
├── tools/                  # 4. 工具目录：所有工具都在这里（可无限扩展）
│   ├── __init__.py         # 工具汇总与注册（核心枢纽）
│   ├── weather_tool.py     # 天气工具的具体实现（高德 API）
│   └── tool_schema.py      # 所有工具的 JSON 说明书
└── requirements.txt        # 5. 依赖管理（记录需要的第三方库）
