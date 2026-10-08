"""
Tests for app/resume_parser.py
"""

import pytest

from app.resume_parser import extract_text_from_pdf


class FakeUploadedFile:
    """Minimal stand-in for Streamlit's UploadedFile."""

    def __init__(self, data: bytes):
        self._data = data

    def read(self):
        return self._data


def test_extract_text_from_invalid_pdf():
    """
    Passing random bytes should raise an error (invalid PDF).
    """
    fake = FakeUploadedFile(b"this is not a real pdf")
    with pytest.raises(Exception):
        extract_text_from_pdf(fake)


def test_extract_text_from_empty_bytes():
    """
    Empty bytes should also fail (fitz cannot open).
    """
    fake = FakeUploadedFile(b"")
    with pytest.raises(Exception):
        extract_text_from_pdf(fake)