# StudyAssistant-AI-Dark 🎓

**A Privacy-Focused Educational AI Assistant with Dark Theme**

## Features ✨
- 🔒 **Privacy-First**: Runs locally, no data collection, open-source
- 🌙 **Dark Theme**: Modern, eye-friendly dark UI
- 🧠 **AI-Powered**: Uses open-source LLM (Ollama/Mistral)
- 📚 **Educational**: Helps explain concepts, not just give answers
- ⚡ **Fast**: Local inference, no API costs
- 🛡️ **Safe**: Transparent code, community-reviewed

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Ollama (for LLM) - https://ollama.ai

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jeshabraham17-svg/StudyAssistant-AI-Dark.git
   cd StudyAssistant-AI-Dark
   ```

2. **Install Ollama** (for running LLM locally)
   - Download from https://ollama.ai
   - Run: `ollama pull mistral` (or your preferred model)

3. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Setup Frontend**
   ```bash
   cd ../frontend
   npm install
   ```

5. **Run the Application**
   
   Terminal 1 - Start Backend:
   ```bash
   cd backend
   source venv/bin/activate
   python app.py
   ```
   
   Terminal 2 - Start Frontend:
   ```bash
   cd frontend
   npm start
   ```

6. **Access the App**
   - Open http://localhost:3000 in your browser

## Architecture 🏗️

```
StudyAssistant-AI-Dark/
├── backend/               # Python Flask API
│   ├── app.py            # Main Flask app
│   ├── llm_handler.py    # LLM integration with Ollama
│   ├── requirements.txt  # Python dependencies
│   └── config.py         # Configuration
├── frontend/             # React web app
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── styles/       # Dark theme CSS
│   │   ├── App.js        # Main app
│   │   └── index.js      # Entry point
│   └── package.json
└── README.md
```

## Usage 📖

1. **Ask Questions**: Type any homework question or topic
2. **Get Explanations**: AI explains concepts step-by-step
3. **Learn More**: Ask follow-up questions for deeper understanding
4. **No Cheating**: AI focuses on teaching, not just answering

### Example Queries
- "Explain photosynthesis"
- "How do I solve quadratic equations?"
- "What is the French Revolution?"
- "Help me understand recursion in programming"

## Privacy & Safety 🔐

✅ **100% Local**: Everything runs on your computer
✅ **No Tracking**: No analytics, no data collection
✅ **No API Calls**: No data sent to external servers
✅ **Open Source**: All code is publicly reviewable
✅ **MIT Licensed**: Free to use and modify

## Technology Stack 🛠️

- **Backend**: Flask (Python)
- **Frontend**: React (JavaScript)
- **LLM**: Ollama + Mistral/Llama2
- **Styling**: Tailwind CSS (Dark Theme)
- **API**: RESTful Flask API

## Models Supported 🤖

The app uses Ollama to run open-source LLMs locally:
- **Mistral** (7B) - Fast & accurate ⭐ Recommended
- **Llama 2** (7B) - Capable & flexible
- **Neural Chat** - Conversational

Switch models by running: `ollama pull model-name`

## Contributing 🤝

We welcome contributions! This is an educational project for learning.

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Roadmap 🚀

- [ ] Support for multiple subjects (Math, Science, History, etc.)
- [ ] Study notes generation
- [ ] Quiz/practice problem generation
- [ ] Dark/Light theme toggle
- [ ] Conversation history
- [ ] Export answers as PDF
- [ ] Mobile app version

## Troubleshooting 🔧

**Q: "Connection refused" error?**
A: Make sure Ollama is running. Start it with: `ollama serve`

**Q: Slow responses?**
A: This depends on your hardware. Smaller models are faster.

**Q: How do I use a different model?**
A: Edit `backend/config.py` and change the MODEL_NAME variable

## License 📄

MIT License - See LICENSE file for details

## Support 💬

Have questions? Open an issue on GitHub!

---

**Made with ❤️ for students who value privacy and learning**
