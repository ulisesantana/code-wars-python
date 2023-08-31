def expand_spaces(words, width):
    return ""


def justify(text, width):
    output = ""
    tmp = []
    for word in text.split():
        next_line_width = len(" ".join(tmp)) + len(word)
        if next_line_width < width:
            tmp.append(word)
        elif next_line_width == width:
            tmp.append(word)
            output += " ".join(tmp) + "\n"
        else:
            output += expand_spaces(tmp, width) + "\n"
            tmp.clear()
            tmp.append(word)

    if tmp:
        output += expand_spaces(tmp, width)
    return output


def test_text_align_justify():
    assert justify('123 45 6', 7) == '123  45\n6'
