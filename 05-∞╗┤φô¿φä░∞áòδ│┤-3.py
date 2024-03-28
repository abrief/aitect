import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        root.title('시스템 모니터')

        # 모니터링 상태
        self.monitoring = False

        # CPU 사용량 라벨
        self.cpu_label = ttk.Label(root, text="CPU 사용량: 준비", font=("Arial", 12))
        self.cpu_label.pack(pady=10)

        # RAM 사용량 라벨
        self.ram_label = ttk.Label(root, text="RAM 사용량: 준비", font=("Arial", 12))
        self.ram_label.pack(pady=10)

        # 시작 버튼
        self.start_button = ttk.Button(root, text="시작", command=self.start_monitoring)
        self.start_button.pack(pady=5)

        # 정지 버튼
        self.stop_button = ttk.Button(root, text="정지", command=self.stop_monitoring)
        self.stop_button.pack(pady=5)

    def update_info(self):
        while self.monitoring:
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent

            self.cpu_label.config(text=f"CPU 사용량: {cpu_usage}%")
            self.ram_label.config(text=f"RAM 사용량: {ram_usage}%")

            # 1초 대기
            time.sleep(1)

    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            # 정보 업데이트를 위한 스레드 시작
            self.update_thread = threading.Thread(target=self.update_info)
            self.update_thread.daemon = True
            self.update_thread.start()

    def stop_monitoring(self):
        self.monitoring = False

# GUI 실행
root = tk.Tk()
app = SystemMonitorApp(root)
root.mainloop()
