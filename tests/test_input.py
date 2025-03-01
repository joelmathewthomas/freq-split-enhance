import pytest
from freqsplit.input.file_reader import read_audio
from freqsplit.input.format_checker import is_supported_format

def test_read_audio():
    file_path = "tests/test_audio/cafe_crowd_talk.aiff"
    audio, sr = read_audio(file_path)
    assert len(audio) > 0
    assert sr > 0

def test_is_supported_format():
    assert is_supported_format("tests/test_audio/cafe_crowd_talk.aiff") == True
    assert is_supported_format("tests/test_audio/unsupported_file.txt") == False