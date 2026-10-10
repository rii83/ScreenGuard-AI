
import subprocess

def send_alert():
    # إرسال إشعار إلى الماك
    subprocess.run([
        "osascript",
        "-e",
        'display notification "تحققي من الكاميرا!" with title "ScreenGuard AI"'
    ])
