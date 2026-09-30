# ComicCraft

ComicCraft is an AI-powered comic story creator.

It converts a story idea into a five-panel comic using:

- FastAPI
- Jinja2
- Google Gemini
- Hugging Face
- Pillow
- FPDF2

The project also contains a Demo Mode for testing without API keys.

---

# Project Flow

User Story Prompt

        ↓

FastAPI

        ↓

Gemini

Five Panel Outline

        ↓

Gemini

Narration + Dialogue

        ↓

Hugging Face

Panel Illustrations

        ↓

Layout Builder

        ↓

PDF Export

        ↓

Comic Preview

---

# Requirements

Install:

Python 3.11 or newer

VS Code

Optional:

Gemini API Key

Hugging Face Token

---

# Windows Installation

Open the project folder in VS Code.

Open:

Terminal → New Terminal

Create virtual environment:

```powershell
py -3.11 -m venv .venv