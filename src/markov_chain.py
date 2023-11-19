def build_markov_chain(data, k=1):
    """
    Markov Chain을 구축합니다. 
    data: 음악 데이터 리스트 (예: 음표의 높이 목록).
    k: Markov Chain에서 고려할 상태의 크기 (기본값 1).
    """
    chain = {}
    for i in range(len(data) - k):
        # 현재 상태와 다음 상태를 정의
        current_state = tuple(data[i:i+k])
        next_state = data[i+k]

        # 현재 상태가 체인에 없으면 추가
        if current_state not in chain:
            chain[current_state] = {}

        # 다음 상태의 빈도를 업데이트
        chain[current_state][next_state] = chain[current_state].get(next_state, 0) + 1

    # 각 상태 전이 확률을 계산
    for state, transitions in chain.items():
        total = sum(transitions.values())
        for state2, count in transitions.items():
            transitions[state2] = count / total

    return chain

def predict_next_state(chain, current_state):
    """
    주어진 현재 상태에 대해 다음 상태를 예측합니다.
    chain: 구축된 Markov Chain.
    current_state: 현재 상태 (튜플).
    """
    if current_state in chain:
        next_states = chain[current_state]
        return max(next_states, key=next_states.get)  # 가장 높은 확률을 가진 상태를 반환
    else:
        return None
