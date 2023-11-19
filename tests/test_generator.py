from markov_chain import build_markov_chain, predict_next_state

# 임의의 시퀀스 생성을 위한 데이터 (예: 파싱된 MIDI 파일로부터 추출된 음표 높이)
notes_data = [60, 62, 64, 65, 67, 65, 64, 62]  # 이것은 예시 데이터입니다.

# Markov Chain 모델 구축
chain = build_markov_chain(notes_data, k=1)

# 시퀀스 생성
generated_sequence = generate_sequence(chain, length=50)

# 생성된 시퀀스 출력
print(generated_sequence)
