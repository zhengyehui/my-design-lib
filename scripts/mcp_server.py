#!/usr/bin/env python3
"""
My Design Lib — MCP Server
让 AI 编程工具直接调用你的设计组件库

使用方式:
  python mcp_server.py          # 启动 MCP Server
  python mcp_server.py --http   # 启动 HTTP 模式（端口 8900）

MCP 工具:
  - list_components: 列出所有可用组件
  - get_component: 获取组件代码
  - get_tokens: 获取设计变量
  - search_components: 按标签搜索组件
"""

import json
import os
import sys
from pathlib import Path

# ─── 配置 ───
LIB_ROOT = Path(__file__).parent.parent
COMPONENTS_DIR = LIB_ROOT / "src" / "components"
TOKENS_DIR = LIB_ROOT / "src" / "tokens"
MANIFEST_PATH = LIB_ROOT / "ai-manifest.json"


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {"components": []}


def list_components() -> str:
    """列出所有可用组件及其变体"""
    manifest = load_manifest()
    result = []
    for comp in manifest.get("components", []):
        variants = ", ".join(comp.get("variants", []))
        result.append(f"• {comp['name']}: {variants} ({comp.get('description', '')})")
    return "\n".join(result) if result else "暂无组件"


def get_component(name: str, variant: str = "") -> str:
    """获取指定组件的 HTML 代码"""
    comp_dir = COMPONENTS_DIR / name
    if not comp_dir.exists():
        return f"组件 '{name}' 不存在"

    html_file = comp_dir / f"{name}.html"
    if not html_file.exists():
        return f"组件 '{name}' 的 HTML 文件不存在"

    content = html_file.read_text()

    # 如果指定了变体，尝试过滤
    if variant:
        # 查找包含变体标记的代码块
        marker_start = f"<!-- variant: {variant} -->"
        marker_end = "<!-- /variant -->"
        start = content.find(marker_start)
        end = content.find(marker_end)
        if start != -1 and end != -1:
            return content[start:end + len(marker_end)]
        else:
            return f"变体 '{variant}' 未找到，返回全部代码:\n\n{content}"

    return content


def get_tokens(format: str = "css") -> str:
    """获取设计变量（css 或 json 格式）"""
    if format == "json":
        token_file = TOKENS_DIR / "tokens.json"
    else:
        token_file = TOKENS_DIR / "tokens.css"

    if not token_file.exists():
        return f"设计变量文件不存在: {token_file}"

    return token_file.read_text()


def search_components(query: str) -> str:
    """按关键词搜索组件"""
    manifest = load_manifest()
    results = []
    query_lower = query.lower()

    for comp in manifest.get("components", []):
        name = comp.get("name", "").lower()
        desc = comp.get("description", "").lower()
        tags = [t.lower() for t in comp.get("tags", [])]

        if query_lower in name or query_lower in desc or any(query_lower in t for t in tags):
            results.append(f"• {comp['name']}: {comp.get('description', '')}")

    return "\n".join(results) if results else f"未找到与 '{query}' 相关的组件"


# ─── MCP 协议实现 ───

MCP_TOOLS = [
    {
        "name": "list_components",
        "description": "列出 My Design Lib 中所有可用的前端组件",
        "inputSchema": {"type": "object", "properties": {}}
    },
    {
        "name": "get_component",
        "description": "获取指定组件的 HTML+CSS 代码，可选指定变体",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "组件名称，如 button, card, hero"},
                "variant": {"type": "string", "description": "可选，组件变体名称"}
            },
            "required": ["name"]
        }
    },
    {
        "name": "get_tokens",
        "description": "获取设计变量（颜色、间距、字体等），支持 CSS 或 JSON 格式",
        "inputSchema": {
            "type": "object",
            "properties": {
                "format": {
                    "type": "string",
                    "enum": ["css", "json"],
                    "default": "css"
                }
            }
        }
    },
    {
        "name": "search_components",
        "description": "按关键词搜索组件，如 'button', 'card', 'form'",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "搜索关键词"}
            },
            "required": ["query"]
        }
    }
]

TOOL_HANDLERS = {
    "list_components": lambda args: list_components(),
    "get_component": lambda args: get_component(args.get("name", ""), args.get("variant", "")),
    "get_tokens": lambda args: get_tokens(args.get("format", "css")),
    "search_components": lambda args: search_components(args.get("query", "")),
}


def run_mcp_stdio():
    """标准 MCP stdio 模式"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = msg.get("method", "")
        msg_id = msg.get("id")

        if method == "initialize":
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "my-design-lib", "version": "1.0.0"}
                }
            }
        elif method == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {"tools": MCP_TOOLS}
            }
        elif method == "tools/call":
            params = msg.get("params", {})
            tool_name = params.get("name", "")
            args = params.get("arguments", {})
            handler = TOOL_HANDLERS.get(tool_name)
            if handler:
                content = handler(args)
                response = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": content}]}
                }
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}
                }
        else:
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Unknown method: {method}"}
            }

        print(json.dumps(response), flush=True)


def run_http(port: int = 8900):
    """简单 HTTP 模式（方便调试）"""
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import urllib.parse

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path
            params = urllib.parse.parse_qs(parsed.query)

            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")

            if path == "/tools":
                result = MCP_TOOLS
            elif path == "/components":
                result = {"components": list_components()}
            elif path == "/component":
                name = params.get("name", [""])[0]
                variant = params.get("variant", [""])[0]
                result = {"html": get_component(name, variant)}
            elif path == "/tokens":
                fmt = params.get("format", ["css"])[0]
                result = {"tokens": get_tokens(fmt)}
            elif path == "/search":
                query = params.get("q", [""])[0]
                result = {"results": search_components(query)}
            elif path == "/health":
                result = {"status": "ok", "name": "my-design-lib"}
            else:
                self.send_response(404)
                self.end_headers()
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode())

        def log_message(self, format, *args):
            pass  # 静默日志

    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"🚀 My Design Lib MCP Server (HTTP) running on http://0.0.0.0:{port}")
    server.serve_forever()


if __name__ == "__main__":
    if "--http" in sys.argv:
        run_http()
    else:
        print("🚀 My Design Lib MCP Server (stdio mode)", file=sys.stderr)
        run_mcp_stdio()
