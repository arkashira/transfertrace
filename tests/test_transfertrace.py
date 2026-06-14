import time
import sys
from io import StringIO
from unittest.mock import patch
import pytest
from transfertrace import TransferProgressBar, simulate_transfer

def test_transfer_progress_bar():
    total_bytes = 1000
    progress_bar = TransferProgressBar(total_bytes)

    with patch('sys.stdout', new=StringIO()) as fake_out:
        progress_bar.update(500)
        output = fake_out.getvalue()
        assert "50.0%" in output
        assert "500/1000" in output
        assert "ETA:" in output

        progress_bar.pause()
        progress_bar.update(600)
        output = fake_out.getvalue()
        assert "50.0%" in output  # Should not update when paused

        progress_bar.resume()
        progress_bar.update(600)
        output = fake_out.getvalue()
        assert "60.0%" in output  # Should update when resumed

def test_simulate_transfer():
    total_bytes = 1000
    progress_callback = lambda x: None

    with patch('sys.stdout', new=StringIO()) as fake_out:
        simulate_transfer(total_bytes, progress_callback, duration=0.1)
        output = fake_out.getvalue()
        assert "Transfer completed!" in output

def test_progress_bar_formatting():
    total_bytes = 1000
    progress_bar = TransferProgressBar(total_bytes)

    with patch('sys.stdout', new=StringIO()) as fake_out:
        progress_bar.update(500)
        output = fake_out.getvalue()
        assert "50.0%" in output
        assert "500/1000" in output
        assert "ETA:" in output

        progress_bar.update(1000)
        output = fake_out.getvalue()
        assert "100.0%" in output
        assert "1000/1000" in output
        assert "ETA: 0s" in output
