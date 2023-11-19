import pretty_midi

def create_midi(sequence, output_file='output.mid', instrument_name='Acoustic Grand Piano'):
    """
    주어진 음악 시퀀스로 MIDI 파일을 생성합니다.
    sequence: 음악 시퀀스 (음표의 높이 목록).
    output_file: 생성된 MIDI 파일의 저장 경로.
    instrument_name: 사용할 악기의 이름.
    """
    # 새로운 PrettyMIDI 객체 생성
    midi = pretty_midi.PrettyMIDI()

    # 사용할 악기를 설정
    instrument_program = pretty_midi.instrument_name_to_program(instrument_name)
    instrument = pretty_midi.Instrument(program=instrument_program)

    # 현재 시간을 추적
    current_time = 0
    note_duration = 0.5  # 음표 지속 시간을 0.5초로 설정

    # 시퀀스에 있는 각 음표에 대해 MIDI 노트를 생성
    for note_number in sequence:
        # MIDI 노트 생성 (시작 시간, 종료 시간, 음표 번호)
        note = pretty_midi.Note(
            velocity=100,  # 음표의 강도
            pitch=note_number,  # 음표의 높이
            start=current_time,
            end=current_time + note_duration
        )
        instrument.notes.append(note)
        current_time += note_duration

    # 생성된 악기를 MIDI 데이터에 추가
    midi.instruments.append(instrument)

    # MIDI 파일 저장
    midi.write(output_file)

# 예시 사용
sequence = [60, 62, 64, 65, 67, 65, 64, 62]  # C 메이저 스케일
create_midi(sequence, 'example.mid')
