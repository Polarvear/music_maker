import sys
import os

# 현재 스크립트의 위치를 기반으로 src 폴더의 절대 경로를 추가합니다.
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, 'src'))

from markov_chain import build_markov_chain, predict_next_state

# 테스트 데이터
test_data = [60, 62, 64, 65, 67, 65, 64, 62]  # 예: C 메이저 스케일

# Markov Chain 구축
chain = build_markov_chain(test_data, k=1)

# 현재 상태 설정 (예: 60)
current_state = (60,)

# 다음 상태 예측
next_state = predict_next_state(chain, current_state)

print("현재 상태:", current_state)
print("예측된 다음 상태:", next_state)
