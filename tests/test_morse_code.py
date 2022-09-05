from morse_code.morse_code import letters_to_morse_code, morse_code_to_letters


def test_letters_to_morse_code():
    assert (
        letters_to_morse_code("Timothy Traddle")
        == "- .. -- --- - .... -.-- / - .-. .- -.. -.. .-.. ."
    )


def test_morse_code_to_letters():
    assert morse_code_to_letters("-.- .. -.. . ---") == "KIDEO"
