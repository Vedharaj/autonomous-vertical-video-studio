#!/usr/bin/env bash
# ==============================================================================
# Google Flow Remote Debugging & MCP Service Manager
# Parameterized service controller reading ports & profile from environment
# ==============================================================================

CHROME_PORT="${CHROME_REMOTE_DEBUG_PORT:-9333}"
CHROME_PROFILE="${CHROME_PROFILE_DIR:-/home/vedha/.flow-mcp/chrome-profile}"
FLOW_MCP_DIR="${FLOW_MCP_PATH:-/media/vedha/E2/mcp/flow-mcp}"
MCP_PORT="${FLOW_MCP_PORT:-8787}"

case "$1" in
  start)
    echo "=== Starting Google Flow Services ==="
    # 1. Start Chrome with remote debugging if not already running
    if curl -s "http://localhost:${CHROME_PORT}/json/version" > /dev/null 2>&1; then
      echo "[OK] Chrome CDP is already running on port ${CHROME_PORT}."
    else
      echo "[START] Launching Chrome on port ${CHROME_PORT} with profile ${CHROME_PROFILE}..."
      google-chrome \
        --remote-debugging-port="${CHROME_PORT}" \
        --user-data-dir="${CHROME_PROFILE}" \
        --no-first-run \
        --no-default-browser-check \
        "https://flow.google.com" > /dev/null 2>&1 &
      sleep 2
    fi

    # 2. Start Flow MCP Daemon if directory exists and not running
    if [ -d "${FLOW_MCP_DIR}" ]; then
      if ss -tulpn 2>/dev/null | grep -q ":${MCP_PORT} "; then
        echo "[OK] flow-mcp daemon is already active on port ${MCP_PORT}."
      else
        echo "[START] Launching flow-mcp daemon on port ${MCP_PORT}..."
        nohup node "${FLOW_MCP_DIR}/dist/index.js" > "/tmp/flow-mcp.log" 2>&1 &
        sleep 1
      fi
    fi
    echo "[SUCCESS] Flow services are ready."
    ;;

  status)
    echo "=== Google Flow Services Status ==="
    echo -n "Chrome CDP (port ${CHROME_PORT}): "
    if curl -s "http://localhost:${CHROME_PORT}/json/version" > /dev/null 2>&1; then
      echo "RUNNING"
      curl -s "http://localhost:${CHROME_PORT}/json/list" | grep -o '"title": "[^"]*"' | head -n 3
    else
      echo "STOPPED"
    fi

    echo -n "Flow MCP Daemon (port ${MCP_PORT}): "
    if ss -tulpn 2>/dev/null | grep -q ":${MCP_PORT} "; then
      echo "RUNNING"
    else
      echo "STOPPED"
    fi
    ;;

  stop)
    echo "=== Stopping Google Flow Services ==="
    pkill -f "flow-mcp/dist/index.js" 2>/dev/null && echo "[STOPPED] flow-mcp"
    pkill -f "remote-debugging-port=${CHROME_PORT}" 2>/dev/null && echo "[STOPPED] Chrome CDP"
    ;;

  *)
    echo "Usage: $0 {start|status|stop}"
    exit 1
    ;;
esac
