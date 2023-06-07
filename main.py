from typing import List
import mido


def isMessageRelevant(message: mido.MetaMessage | mido.Message) -> bool:
    if isinstance(message, mido.MetaMessage):
        return False
    if message.type != 'note_on':
        return False
    # if message.velocity == 0:
        # return False
    return True


def convert_value_to_note(value: int) -> str:
    if value == 21:
        return "A0"
    if value == 22:
        return "A#0"
    if value == 23:
        return "B0"
    octave: int = (value - 24) // 12 + 1
    note_index: int = (value - 24) % 12
    return notes[note_index] + str(octave)


notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

mid: mido.MidiFile = mido.MidiFile('./midi_samples/sample_1.mid')

track: mido.MidiTrack = mid.tracks[0]

messages: List[mido.Message] = list(filter(isMessageRelevant, track))


# for message in messages:
#     print(f"{convert_value_to_note(message.note)}: {message.time}")

# note_plays = {}
# for message in messages:
#     note_play = {"on": message.velocity != 0, "duration": message.time}
#     if message.note in note_plays:
#         note_plays[message.note].append(note_play)
#     else:
#         note_plays[message.note] = [note_play]

# f = open("./outputs/sample_1_output.txt", "w")
# sorted_keys = list(note_plays.keys())
# sorted_keys.sort()
# for key in sorted_keys:
#     plays = note_plays[key]
#     f.write(f"{convert_value_to_note(key):<5}: ")
#     for play in plays:
#         ch = 'X' if play["on"] else '.'
#         str_val = ch * play["duration"]
#         f.write(str_val)
#     f.write("\n")

# for note in note_plays:
#     print(note)

# print(convert_value_to_note(22))
# print(convert_value_to_note(24))
# print(convert_value_to_note(36))
# print(convert_value_to_note(40))
# print(convert_value_to_note(66))
# print(convert_value_to_note(84))
# print(convert_value_to_note(100))

# plays = {key: {"state": False, "values": []} for key in range(21, 109)}
# assume all keys start with the false state, which means none are playing.
# the state can flip only when message tells so
# messages are received only when dT becomes 0
# take first message, take dT from it. When dT becomes 0, read a new message
# the state determines the value at the tick


# Too inefficient
# while True:
#     message = messages.pop(0)
#     dT = message.time
#     # this should change only if the velocity goes to 0
#     plays[message.note]["state"] = not plays[message.note]["state"]
#     for _ in range(dT):
#         for play_key in plays:
#             play = plays[play_key]
#             play["values"].append(play["state"])
#     if len(messages) == 6000:
#         break

# for play in plays:
#     print(play)

key_presses = {key: [] for key in range(21, 109)}
pressed_down_keys = []
current_tick = 0
while True:
    message: mido.Message = messages.pop(0)
    dT = message.time
    if message.
    if len(messages) == 0:
        break
