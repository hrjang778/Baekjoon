import pyautogui
import pyperclip  # 클립보드 제어를 위한 모듈
import time

# 메시지 리스트 (24가지 경우의 수)
messages = [
    '영은 지예 가연 만옥', 
    '영은 지예 만옥 가연', 
    '영은 가연 지예 만옥', 
    '영은 가연 만옥 지예', 
    '영은 만옥 지예 가연', 
    '영은 만옥 가연 지예', 
    '지예 영은 가연 만옥', 
    '지예 영은 만옥 가연', 
    '지예 가연 영은 만옥', 
    '지예 가연 만옥 영은', 
    '지예 만옥 영은 가연', 
    '지예 만옥 가연 영은', 
    '가연 영은 지예 만옥', 
    '가연 영은 만옥 지예', 
    '가연 지예 영은 만옥', 
    '가연 지예 만옥 영은', 
    '가연 만옥 영은 지예', 
    '가연 만옥 지예 영은', 
    '만옥 영은 지예 가연', 
    '만옥 영은 가연 지예', 
    '만옥 지예 영은 가연', 
    '만옥 지예 가연 영은', 
    '만옥 가연 영은 지예', 
    '만옥 가연 지예 영은'
]

# 좌표를 수동으로 입력 (카카오톡 메시지 창의 좌표)
input_x, input_y = -736, 1373  # 이 부분은 find_position()으로 얻은 좌표로 교체해야 합니다

# Alt + Tab으로 창을 활성화하고 메시지를 입력
# pyautogui.hotkey('alt', 'tab')  # 카카오톡 창으로 전환
# time.sleep(1)  # 창 전환 후 대기

for message in messages:
    pyautogui.click(input_x, input_y)  # 입력창 클릭 (좌표가 정확한지 확인 필요)
    time.sleep(0.5)  # 클릭 후 대기
    
    pyperclip.copy(message)  # 메시지를 클립보드에 복사
    pyautogui.hotkey('ctrl', 'v')  # 클립보드의 내용을 붙여넣기
    pyautogui.press('enter')  # Enter 키로 메시지 전송
    
    time.sleep(0.1)  # 5초 대기
