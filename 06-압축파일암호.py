import zipfile2


def crack_zip_password(zip_filepath):
    # ZIP 파일을 열기
    zip_file = zipfile2.ZipFile(zip_filepath)

    # 1부터 5자리 숫자까지 모든 가능성 시도
    for length in range(1, 6):
        for i in range(10 ** length):
            # 현재 시도하는 암호 생성
            password = str(i).zfill(length)

            try:
                # 암호를 바이트로 변환하여 시도
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                print(f"Password found: {password}")
                return password
            except:
                continue  # 암호가 틀리면 계속 시도

    print("Password not found.")
    return None


# 사용 예
zip_filepath = '/Users/cedek/Documents/Python/pythonProject1/암호문서.zip'  # ZIP 파일 경로를 여기에 입력하세요.
crack_zip_password(zip_filepath)
