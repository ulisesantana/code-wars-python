def expand_spaces(words, width):
    if len(words) == 1:
        return words[0]
    missing_spaces = width - len(" ".join(words))
    if len(words) == 2:
        return f"{words[0]}{' ' * (missing_spaces + 1)}{words[1]}"
    output = ""
    max_spaces = len(words) - 1
    if missing_spaces > max_spaces:
        last_word_index = len(words) - 1
        return expand_spaces(
            [f"{word} " if i < last_word_index else word for i, word in enumerate(words)],
            width
        )
    for word in words[0:missing_spaces]:
        output += f"{word}  "
    output += " ".join(words[missing_spaces:])
    return output.strip()


def justify(text, width):
    output = ""
    tmp = []
    words = text.split()
    last_word_index = len(words) - 1
    for i, word in enumerate(words):
        next_line_width = len(" ".join(tmp)) + len(f" {word}")
        if next_line_width < width:
            tmp.append(word)
        elif next_line_width == width:
            tmp.append(word)
            if i == last_word_index:
                output += " ".join(tmp)
            else:
                output += " ".join(tmp) + "\n"
            tmp.clear()
        else:
            output += expand_spaces(tmp, width) + "\n"
            tmp = [word]

    if tmp:
        output += " ".join(tmp)
    return output


def test_text_align_justify():
    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, ' \
                  'at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet ' \
                  'felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt ' \
                  'suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. ' \
                  'Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec ' \
                  'lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis ' \
                  'rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque ' \
                  'commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et ' \
                  'dolor.'
    assert justify('123 45 6', 7) == '123  45\n6'
    assert justify(lorem_ipsum, 30) == """Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""
    assert justify(lorem_ipsum, 15) == """Lorem     ipsum
dolor sit amet,
consectetur
adipiscing
elit.
Vestibulum
sagittis  dolor
mauris,      at
elementum
ligula   tempor
eget.  In  quis
rhoncus   nunc,
at      aliquet
orci.  Fusce at
dolor  sit amet
felis  suscipit
tristique.  Nam
a     imperdiet
tellus.   Nulla
eu   vestibulum
urna.   Vivamus
tincidunt
suscipit  enim,
nec    ultrices
nisi   volutpat
ac.    Maecenas
sit        amet
lacinia   arcu,
non      dictum
justo.    Donec
sed   quam  vel
risus  faucibus
euismod.
Suspendisse
rhoncus rhoncus
felis        at
fermentum.
Donec     lorem
magna,
ultricies     a
nunc  sit amet,
blandit
fringilla nunc.
In   vestibulum
velit  ac felis
rhoncus
pellentesque.
Mauris       at
tellus    enim.
Aliquam
eleifend tempus
dapibus.
Pellentesque
commodo,   nisi
sit        amet
hendrerit
fringilla, ante
odio      porta
lacus,       ut
elementum justo
nulla et dolor."""
