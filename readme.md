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
