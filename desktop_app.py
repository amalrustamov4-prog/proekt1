import sys
import os
import time
import socket
import threading
import subprocess
import uvicorn
import webbrowser

def is_port_in_use(port: int = 8000, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

def start_backend_server():
    """Runs FastAPI uvicorn server in a daemon thread."""
    if not is_port_in_use(8000):
        print("[BizCore] Starting local backend server on http://127.0.0.1:8000...")
        uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="error")

def get_browser_executable() -> str | None:
    """Finds installed Microsoft Edge or Google Chrome to run in standalone Window App Mode."""
    potential_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
    ]
    for path in potential_paths:
        if os.path.exists(path):
            return path
    return None

def launch_standalone_window(url: str):
    """
    Launches a dedicated, standalone, frameless Windows Desktop Application Window
    without browser address bar or tabs.
    """
    browser_exe = get_browser_executable()
    user_data_dir = os.path.join(os.path.expanduser("~"), ".bizcore_desktop_profile")
    os.makedirs(user_data_dir, exist_ok=True)

    if browser_exe:
        print(f"[BizCore] Launching Desktop Window using: {os.path.basename(browser_exe)}")
        cmd = [
            browser_exe,
            f"--app={url}",
            f"--user-data-dir={user_data_dir}",
            "--window-size=1320,860",
            "--window-position=120,60",
            "--disable-extensions",
            "--disable-plugins",
            "--no-first-run",
            "--no-default-browser-check"
        ]
        process = subprocess.Popen(cmd)
        process.wait()
    else:
        # Fallback to default system browser
        print("[BizCore] Opening default browser...")
        webbrowser.open(url)

def main():
    print("=========================================================")
    print("          🚀 BizCore UZ — Windows Desktop Edition")
    print("=========================================================")
    
    # 1. Start backend server in daemon background thread
    server_thread = threading.Thread(target=start_backend_server, daemon=True)
    server_thread.start()

    # 2. Wait until backend server is responsive
    url = "http://127.0.0.1:8000"
    retries = 0
    while not is_port_in_use(8000) and retries < 25:
        time.sleep(0.2)
        retries += 1

    time.sleep(0.3)
    print(f"[BizCore] Backend online. Opening Windows App at {url}...")

    # 3. Launch the dedicated standalone Desktop Window
    try:
        launch_standalone_window(url)
    except KeyboardInterrupt:
        print("[BizCore] Shutting down...")
    except Exception as e:
        print(f"[BizCore] Error launching app window: {e}")
        webbrowser.open(url)

if __name__ == "__main__":
    main()
