<h3 align="center">🛠️ transfertrace</h3>

<div align="center">
  <a href="https://github.com/axentx/transfertrace/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/axentx/transfertrace">
    <img src="https://img.shields.io/badge/language-Python-blue.svg" alt="Language: Python">
  </a>
  <a href="https://github.com/axentx/transfertrace/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/axentx/transfertrace/build.yml?branch=main" alt="Build Status">
  </a>
  <a href="https://github.com/axentx/transfertrace/stargazers">
    <img src="https://img.shields.io/github/stars/axentx/transfertrace" alt="Stars">
  </a>
</div>

---
# 🚀 transfertrace
**Power developers and system operators with real-time file transfer monitoring and progress tracking.** TransferTrace is a Python CLI utility that shows a real-time progress bar and detailed stats for file transfer operations.

## Why transfertrace?
- **Real-time monitoring**: Get instant feedback on file transfer progress, including percentage completed, transferred bytes, total size, and estimated time remaining.
- **Pause and resume**: Pause and resume the tracking without affecting the underlying transfer.
- **Coexists with logging output**: TransferTrace writes its UI to a separate stream, allowing it to coexist with existing logging output.
- **Lightweight**: TransferTrace is a small Python module with minimal dependencies.
- **Flexible**: Use TransferTrace with existing file copy, download, or upload commands in scripts or terminal sessions.
- **Easy to use**: Simple command-line interface makes it easy to get started.
- **Open-source**: TransferTrace is open-source, allowing for community contributions and customization.

## Feature Overview
| Feature | Description |
| --- | --- |
| Real-time progress bar | Displays a live progress bar for file transfers |
| Detailed stats | Shows percentage completed, transferred bytes, total size, and estimated time remaining |
| Pause and resume | Allows pausing and resuming the tracking without affecting the underlying transfer |
| Coexists with logging output | Writes UI to a separate stream, allowing coexistence with existing logging output |

## Tech Stack
* Python

## Project Structure
* business: Business-related files
* docs: Documentation files
* src: Source code files
* tests: Test files

## Getting Started
```bash
# Install dependencies
pip install -r requirements.txt

# Run TransferTrace
python -m transfertrace --help
```

## Deploy
```bash
# Build and deploy TransferTrace
python -m build
python -m twine upload dist/*
```

## Status
TransferTrace is currently in the early stage of development. Recent commits include:
* feat(transfertrace): reconcile sandbox-tested implementation
* axentx-dev-bot: docs cycle 20260610-101456-transfer
* axentx-dev-bot: docs cycle 20260610-095929-transfer
* axentx-dev-bot: docs cycle 20260610-095208-transfer
* axentx-dev-bot: code-build cycle 20260610-080943-transfer
* Initial commit

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to TransferTrace.

## License
TransferTrace is licensed under the MIT License. See [LICENSE](LICENSE) for details.