import requests
import json
from config import OLLAMA_BASE_URL, MODEL_NAME, TEMPERATURE, MAX_TOKENS, TOP_P

class OllamaHandler:
    """
    Handles communication with Ollama LLM
    """
    
    def __init__(self):
        self.base_url = OLLAMA_BASE_URL
        self.model = MODEL_NAME
        self.temperature = TEMPERATURE
        self.max_tokens = MAX_TOKENS
        self.top_p = TOP_P
    
    def check_connection(self):
        """
        Check if Ollama is running
        """
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def generate_response(self, user_message, conversation_history=None):
        """
        Generate a response from the LLM
        
        Args:
            user_message: User's question/prompt
            conversation_history: List of previous messages for context
        
        Returns:
            dict with response text and metadata
        """
        
        # Build the prompt with system instructions
        system_prompt = """You are an educational AI tutor designed to help students learn. 
Your goal is to:
1. Explain concepts clearly and simply
2. Help students understand, not just give answers
3. Ask guiding questions to deepen understanding
4. Break down complex topics into digestible parts
5. Encourage critical thinking

Always be encouraging and supportive. If asked to do homework for the student, politely redirect them to learn the concept instead."""
        
        # Build messages
        messages = []
        if conversation_history:
            messages.extend(conversation_history)
        messages.append({"role": "user", "content": user_message})
        
        # Format for Ollama
        full_prompt = system_prompt + "\n\n"
        for msg in messages:
            role = msg["role"].upper()
            full_prompt += f"{role}: {msg['content']}\n"
        full_prompt += "ASSISTANT: "
        
        try:
            # Call Ollama API
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    "temperature": self.temperature,
                    "top_p": self.top_p,
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "response": result.get("response", "").strip(),
                    "model": self.model,
                    "timestamp": result.get("created_at", "")
                }
            else:
                return {
                    "success": False,
                    "error": f"Ollama error: {response.status_code}",
                    "response": None
                }
        
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timeout - Ollama might be overloaded",
                "response": None
            }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Cannot connect to Ollama. Make sure it's running: ollama serve",
                "response": None
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error: {str(e)}",
                "response": None
            }

# Initialize handler
ollama_handler = OllamaHandler()
