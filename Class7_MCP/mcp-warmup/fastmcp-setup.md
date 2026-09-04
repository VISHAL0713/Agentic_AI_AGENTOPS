# FastMCP + MCP Inspector — Environment Setup Reference

## Prerequisite versions

| Tool | Minimum version | Why |
|---|---|---|
| Python | 3.11+ | FastMCP requires 3.11+ (some environments test up to 3.14) |
| Node.js | 22.19.0+ | `@modelcontextprotocol/inspector@2.5.0` requires `>=22.19.0` |
| npm | 10.x+ (bundled with Node 20/22) | npm 9.x and earlier has a known Arborist bug (`edgesOut` crash) resolving deep/optional peer dependencies |
| uv | latest | Manages the Python virtualenv + dependencies per-project |

Check what you currently have:
```bash
python --version
node -v
npm -v
uv --version
```

---

## 1. Install `uv` (Python package/env manager)

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Via pip (any platform, if you already have Python):**
```bash
pip install uv
```

Verify:
```bash
uv --version
```

---

## 2. Set up the project with `uv`

```bash
uv init mcp-warmup
cd mcp-warmup
uv add fastmcp
```

This creates `pyproject.toml`, a `.venv`, and locks `fastmcp` as a dependency.

Verify the dependency resolved correctly:
```bash
uv run python -c "import fastmcp; print(fastmcp.__version__)"
```

Run your server directly through uv (uses the project's `.venv` automatically):
```bash
uv run python server.py
```

---

## 3. Install/verify Node.js + npm (needed for `npx` and MCP Inspector)

### Install nvm-windows (Windows) — recommended over a standalone Node installer
1. Download `nvm-setup.exe` from: https://github.com/coreybutler/nvm-windows/releases (under "Assets" of the latest release)
2. Run the installer, then **close and reopen your terminal**
3. If you already have a standalone Node.js install (`C:\Program Files\nodejs` as a real folder, not a symlink), **uninstall it first** — nvm-windows needs to own that path.

### Install a compatible Node version
```bash
nvm install 22.19.0
nvm use 22.19.0
```

### macOS / Linux — use standard `nvm`
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install 22
nvm use 22
```

Verify:
```bash
node -v      # should be >=22.19.0
npm -v       # should be 10.x+
```

---

## 4. Run MCP Inspector against your FastMCP server

Route Inspector through `uv run` so it uses your project's `.venv` (not whatever `python` happens to be on PATH — this avoids `ModuleNotFoundError: No module named 'fastmcp'`):

```bash
npx @modelcontextprotocol/inspector@2.5.0 uv run python server.py
```

---

## Common issues & fixes

**`npm ERR! Cannot read properties of null (reading 'edgesOut')`**
Known npm 8/9 bug resolving deep optional peer dependencies. Fix: upgrade to npm 10+ (comes with Node 20+).
```bash
npm cache clean --force
```
If that alone doesn't fix it, the real fix is upgrading Node/npm as above.

**`npm warn EBADENGINE` / native binding errors**
Node version too old for the package. Bump Node via nvm to the version the warning specifies.

**`ModuleNotFoundError: No module named 'fastmcp'`**
The `python` being invoked isn't the one with `fastmcp` installed. Use `uv run python server.py` (or the full path from `uv run which python`) instead of bare `python`.

**Conda shadowing nvm's Node**
If `(base)` or another conda env is active, conda's own `node`/`npm` (if installed) can sit earlier in PATH than nvm's. Run `which node` to check; `conda deactivate` (possibly twice) if needed.
