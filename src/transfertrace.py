import time
import sys
from dataclasses import dataclass
from typing import Optional, Callable

@dataclass
class TransferProgress:
    transferred_bytes: int = 0
    total_bytes: int = 0
    start_time: Optional[float] = None
    paused: bool = False

class TransferProgressBar:
    def __init__(self, total_bytes: int):
        self.progress = TransferProgress(total_bytes=total_bytes)
        self._last_update_time = 0
        self._paused_time = 0
        self._total_paused_time = 0

    def update(self, transferred_bytes: int) -> None:
        if self.progress.paused:
            return

        self.progress.transferred_bytes = transferred_bytes
        if self.progress.start_time is None:
            self.progress.start_time = time.time()

        current_time = time.time()
        elapsed_time = current_time - self.progress.start_time - self._total_paused_time
        if elapsed_time > 0:
            speed = transferred_bytes / elapsed_time
            remaining_bytes = self.progress.total_bytes - transferred_bytes
            if speed > 0:
                estimated_time_remaining = remaining_bytes / speed
            else:
                estimated_time_remaining = 0

            self._update_progress_bar(transferred_bytes, self.progress.total_bytes, estimated_time_remaining)

    def pause(self) -> None:
        if not self.progress.paused and self.progress.start_time is not None:
            current_time = time.time()
            self._paused_time = current_time - (self.progress.start_time + self._total_paused_time)
            self.progress.paused = True

    def resume(self) -> None:
        if self.progress.paused:
            current_time = time.time()
            self._total_paused_time += self._paused_time
            self.progress.paused = False
            self.progress.start_time = current_time - self._total_paused_time

    def _update_progress_bar(self, transferred_bytes: int, total_bytes: int, estimated_time_remaining: float) -> None:
        percentage = (transferred_bytes / total_bytes) * 100
        bar_length = 50
        filled_length = int(bar_length * transferred_bytes // total_bytes)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write('\r')
        sys.stdout.write(f'[{bar}] {percentage:.1f}% | {transferred_bytes}/{total_bytes} bytes | ETA: {self._format_time(estimated_time_remaining)}')
        sys.stdout.flush()

    def _format_time(self, seconds: float) -> str:
        if seconds < 1:
            return "0s"
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            return f"{int(hours)}h {int(minutes)}m"
        elif minutes > 0:
            return f"{int(minutes)}m {int(seconds)}s"
        else:
            return f"{int(seconds)}s"

def simulate_transfer(total_bytes: int, progress_callback: Callable[[int], None], duration: float = 5.0) -> None:
    progress_bar = TransferProgressBar(total_bytes)
    start_time = time.time()

    for transferred_bytes in range(0, total_bytes + 1, total_bytes // 100):
        progress_callback(transferred_bytes)
        progress_bar.update(transferred_bytes)
        time.sleep(duration / (total_bytes // 100))

    print("\nTransfer completed!")
