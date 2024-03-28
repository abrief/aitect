import psutil
import time


def monitor_system(duration=5, interval=1):
    start_time = time.time()

    while True:
        # 현재 시간과 시작 시간의 차이
        elapsed_time = time.time() - start_time

        # 지정된 시간이 경과했으면 루프 종료
        if elapsed_time > duration:
            break

        # CPU 사용량
        cpu_usage = psutil.cpu_percent()

        # RAM 사용량
        ram_usage = psutil.virtual_memory().percent

        # 네트워크 패킷 전송량 (바이트 단위)
        net_io = psutil.net_io_counters()
        sent_bytes = net_io.bytes_sent
        recv_bytes = net_io.bytes_recv

        print(f"CPU 사용량: {cpu_usage}%, RAM 사용량: {ram_usage}%, 전송된 바이트: {sent_bytes}, 받은 바이트: {recv_bytes}")

        # 지정된 간격만큼 대기
        time.sleep(interval)


# 5초 동안 모니터링 시작
monitor_system()
