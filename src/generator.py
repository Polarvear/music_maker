import random

def build_markov_chain(data, k=1):
    """ Markov Chain을 구축합니다. 여기서 k는 상태의 크기를 나타냅니다. """
    chain = {}
    for i in range(len(data) - k):
        state = tuple(data[i:i+k])
        next_state = data[i+k]
        if state not in chain:
            chain[state] = {}
        if next_state not in chain[state]:
            chain[state][next_state] = 1
        else:
            chain[state][next_state] += 1
    return chain

def generate_sequence(chain, length=50):
    """ 생성된 Markov Chain을 사용하여 새로운 음악 시퀀스를 생성합니다. """
    state = random.choice(list(chain.keys()))
    sequence = list(state)
    for i in range(length - len(state)):
        next_states = chain.get(state, None)
        if not next_states:
            break
        next_state = random.choices(list(next_states.keys()), weights=next_states.values())[0]
        sequence.append(next_state)
        state = tuple(sequence[-len(state):])
    return sequence

# 예시 사용법
# 'parsed_data'는 파싱된 MIDI 데이터를 나타냅니다. 예를 들어, 이는 음표의 목록일 수 있습니다.
parsed_data = [...]  # 여기에 파싱된 MIDI 데이터를 넣습니다.

# Markov Chain 구축
markov_chain = build_markov_chain([note['pitch'] for note in parsed_data], k=2)

# 새로운 시퀀스 생성
new_sequence = generate_sequence(markov_chain, length=100)

print(new_sequence)
