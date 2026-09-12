from flask import Flask, request, jsonify
from flask_cors import CORS
from llm_handler import ollama_handler
from config import API_PORT, API_HOST, ALLOWED_ORIGINS
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Setup CORS (only allow localhost for security)
CORS(app, resources={
    r"/api/*": {
        "origins": ALLOWED_ORIGINS,
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})

# Store conversation history (in production, use a database)
conversations = {}

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Check if API and LLM are healthy
    """
    ollama_connected = ollama_handler.check_connection()
    
    return jsonify({
        "status": "healthy" if ollama_connected else "degraded",
        "api": "online",
        "ollama": "connected" if ollama_connected else "disconnected",
        "model": ollama_handler.model
    }), 200 if ollama_connected else 503

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint - receives user message and returns AI response
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Missing 'message' field"}), 400
        
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Get conversation history
        history = conversations.get(session_id, [])
        
        # Generate response
        result = ollama_handler.generate_response(user_message, history)
        
        if result['success']:
            # Store in conversation history
            history.append({"role": "user", "content": user_message})
            history.append({"role": "assistant", "content": result['response']})
            
            # Keep only last 10 exchanges to save memory
            if len(history) > 20:
                history = history[-20:]
            
            conversations[session_id] = history
            
            return jsonify({
                "success": True,
                "response": result['response'],
                "model": result['model'],
                "session_id": session_id
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": result['error']
            }), 500
    
    except Exception as e:
        logger.error(f"Error in /api/chat: {str(e)}")
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/api/history/<session_id>', methods=['GET'])
def get_history(session_id):
    """
    Get conversation history for a session
    """
    history = conversations.get(session_id, [])
    return jsonify({
        "session_id": session_id,
        "history": history
    }), 200

@app.route('/api/history/<session_id>', methods=['DELETE'])
def clear_history(session_id):
    """
    Clear conversation history for a session
    """
    if session_id in conversations:
        del conversations[session_id]
    
    return jsonify({
        "success": True,
        "message": f"History cleared for session {session_id}"
    }), 200

@app.route('/api/models', methods=['GET'])
def get_models():
    """
    Get available models from Ollama
    """
    try:
        response = ollama_handler.check_connection()
        return jsonify({
            "current_model": ollama_handler.model,
            "available": response
        }), 200
    except:
        return jsonify({"error": "Cannot fetch models"}), 500

if __name__ == '__main__':
    logger.info(f"Starting StudyAssistant API...")
    logger.info(f"Using model: {ollama_handler.model}")
    logger.info(f"Ollama base URL: {ollama_handler.base_url}")
    
    # Check Ollama connection
    if ollama_handler.check_connection():
        logger.info("✓ Ollama is connected!")
    else:
        logger.warning("✗ Ollama is NOT running. Start it with: ollama serve")
    
    app.run(host=API_HOST, port=API_PORT, debug=True)
