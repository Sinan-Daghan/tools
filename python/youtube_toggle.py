import subprocess

def get_window_id(window_name):
    try:
        window_id = subprocess.check_output(["xdotool", "search", "--name", window_name]).decode("utf-8").strip()
        return window_id
    except subprocess.CalledProcessError:
        return None

if __name__ == "__main__": 
    current_window_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode('utf-8').strip()
    chrome_window_id = get_window_id("Google Chrome")
    subprocess.run(['xdotool', 'windowactivate', chrome_window_id, 'key', 'space', 'windowactivate', current_window_id]) 