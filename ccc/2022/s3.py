import sys

note_count, max_note, sample_count = [int(x) for x in input().split()]

notes = [None] * note_count
remaining_sample_count = sample_count - note_count

if sample_count < note_count or sample_count > (2 * note_count) - 1:
    print(-1)
    sys.exit()

prev = None
for i in range(note_count):

    if not prev:
        prev = "1"
        notes[i] = "1"
        continue

    if remaining_sample_count <= 0:
        notes[i] = prev
        continue
    else:
        if prev == "1":
            notes[i] = "2"
            prev = "2"
        else:
            notes[i] = "1"
            prev = "1"
        remaining_sample_count -= 1

print(" ".join(notes))
