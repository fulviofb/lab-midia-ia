"""Cliente mínimo do MCP do ComfyArt (JSON-RPC por HTTP, só 127.0.0.1).
uso: python mcp_cli.py <projeto> tools
     python mcp_cli.py <projeto> call <ferramenta> '<json de argumentos>'  (ou @arquivo.json)
"""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def rpc(projeto, metodo, params=None, sessao=None, id_=1):
    corpo = {"jsonrpc": "2.0", "method": metodo, "params": params or {}}
    if id_ is not None:
        corpo["id"] = id_
    cab = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if sessao:
        cab["Mcp-Session-Id"] = sessao
    req = urllib.request.Request(f"http://127.0.0.1:8188/comfyart/mcp?project={projeto}", json.dumps(corpo).encode(), cab)
    try:
        r = urllib.request.urlopen(req, timeout=600)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:800]}")
    txt = r.read().decode()
    return (json.loads(txt) if txt.strip() else {}), r.headers.get("Mcp-Session-Id")


def conectar(projeto):
    _, sessao = rpc(projeto, "initialize", {"protocolVersion": "2025-03-26", "capabilities": {},
                                            "clientInfo": {"name": "teste-local", "version": "1"}})
    rpc(projeto, "notifications/initialized", sessao=sessao, id_=None)
    return sessao


if __name__ == "__main__":
    projeto, acao = sys.argv[1], sys.argv[2]
    sessao = conectar(projeto)
    if acao == "tools":
        res, _ = rpc(projeto, "tools/list", sessao=sessao)
        for t in res["result"]["tools"]:
            props = ", ".join(t.get("inputSchema", {}).get("properties", {}))
            print(f"- {t['name']}({props})")
    else:
        bruto = sys.argv[4] if len(sys.argv) > 4 else "{}"
        args = json.loads(Path(bruto[1:]).read_text(encoding="utf-8")) if bruto.startswith("@") else json.loads(bruto)
        res, _ = rpc(projeto, "tools/call", {"name": sys.argv[3], "arguments": args}, sessao)
        if "error" in res:
            print("ERRO", json.dumps(res["error"], ensure_ascii=False)[:1500])
        else:
            for c in res["result"].get("content", []):
                print(c.get("text", f"[{c.get('type')}]"))
