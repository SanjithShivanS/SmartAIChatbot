# Project Summary: SKASC Smart Assistant

## Current Status: COMPLETED (Phase 1-3)
The project is fully functional and customized for **Sri Krishna Arts and Science College (SKASC)**.

## Technical Stack:
- **Backend**: Django 6.0
- **Database**: MySQL (Local)
- **AI Engine**: Gemini (gemini-flash-latest)
- **NLP**: Hybrid (TF-IDF Cosine Similarity for local FAQs + Gemini for general queries)
- **Frontend**: Full-screen HTML/CSS with SKASC branding (Yellow/Blue theme)

## Key Features Implemented:
1. **Contextual Memory**: The bot remembers the last 3 exchanges.
2. **Professional UI**: Full-screen design with SKASC logo, quick buttons, and smooth animations.
3. **Legal Ready**: Disclaimer added to the footer; `.gitignore` created to protect API keys.
4. **Custom Dataset**: Seeded with real SKASC data (NIRF #50, 51 Programs, 13.72 LPA placements).

## Next Step (Future Goal):
- **Make it Public**: Deploying to PythonAnywhere and setting up a cloud MySQL database.

## How to resume:
Ask Gemini CLI to read this file and the `chatbot/nlp_engine.py` to understand the current logic.
