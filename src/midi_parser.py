import pretty_midi

def parse_midi(file_path):

    # MIDI 파일 로드
    midi_data = pretty_midi.PrettyMIDI(file_path)

    # MIDI 파일에서 추출할 데이터를 저장할 구조
    data = {
        'tempo': [],  # 템포 정보
        'notes': []   # 음표 정보
    }

    # 템포 추출
    tempo_changes = midi_data.get_tempo_changes()
    data['tempo'] = tempo_changes[1].tolist()

    # 각 트랙의 음표 추출
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            note_data = {
                'start': note.start,  # 시작 시간
                'end': note.end,      # 종료 시간
                'pitch': note.pitch,  # 음 높이
                'velocity': note.velocity  # 음 세기
            }
            data['notes'].append(note_data)

    return data

# 사용 예
midi_file = r'C:\Users\znzpz\WebstormProjects\MusicComposerPython\data\genre1\merry.mid'
parsed_data = parse_midi(midi_file)
print(parsed_data)
