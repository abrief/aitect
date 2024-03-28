import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        root.title('시스템 모니터')

        # CPU 사용량 라벨
        self.cpu_label = ttk.Label(root, text="CPU 사용량: 계산 중...", font=("Arial", 12))
        self.cpu_label.pack(pady=10)

        # RAM 사용량 라벨
        self.ram_label = ttk.Label(root, text="RAM 사용량: 계산 중...", font=("Arial", 12))
        self.ram_label.pack(pady=10)

        # 정보 업데이트를 위한 스레드 시작
        self.update_thread = threading.Thread(target=self.update_info)
        self.update_thread.daemon = True  # 프로그램 종료 시 스레드도 종료되도록 설정
        self.update_thread.start()

    def update_info(self):
        while True:
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent

            self.cpu_label.config(text=f"CPU 사용량: {cpu_usage}%")
            self.ram_label.config(text=f"RAM 사용량: {ram_usage}%")

            # 1초 대기
            time.sleep(1)

# GUI 실행
root = tk.Tk()
app = SystemMonitorApp(root)
root.mainloop()
