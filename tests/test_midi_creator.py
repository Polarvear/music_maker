import sys
import os

# 현재 스크립트의 위치를 기반으로 src 폴더의 절대 경로를 추가합니다.
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, 'src'))

from midi_creator import create_midi

# 임의의 시퀀스 생성 (여기서는 C 메이저 스케일을 나타냅니다)
sequence = [60, 62, 64, 65, 67, 65, 64, 62]  # MIDI 노트 번호

# MIDI 파일 생성 및 저장
create_midi(sequence, 'output/output.mid')

print("MIDI 파일이 생성되었습니다.")
