import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import ChatMessage from './components/ChatMessage';
import InputBox from './components/InputBox';
import Header from './components/Header';
import StatusBar from './components/StatusBar';
import './styles/App.css';

const API_BASE_URL = 'http://localhost:5000/api';

function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'assistant',
      content: '👋 Welcome to StudyAssistant AI!\n\nI\'m here to help you learn and understand concepts better. Ask me any questions about your homework, subjects, or topics you\'re studying.\n\n💡 Tips:\n• Ask for explanations, not answers\n• I\'ll guide you to understand concepts\n• Feel free to ask follow-up questions',
      timestamp: new Date()
    }
  ]);
  
  const [isLoading, setIsLoading] = useState(false);
  const [apiStatus, setApiStatus] = useState('checking');
  const [sessionId] = useState('default-session');
  const messagesEndRef = useRef(null);
  const [inputValue, setInputValue] = useState('');

  // Check API health on mount
  useEffect(() => {
    checkApiHealth();
    const interval = setInterval(checkApiHealth, 10000); // Check every 10 seconds
    return () => clearInterval(interval);
  }, []);

  // Scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const checkApiHealth = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/health`);
      setApiStatus(response.data.ollama === 'connected' ? 'connected' : 'disconnected');
    } catch (error) {
      setApiStatus('disconnected');
    }
  };

  const handleSendMessage = async (userMessage) => {
    if (!userMessage.trim()) return;

    // Add user message to chat
    const newUserMessage = {
      id: messages.length + 1,
      type: 'user',
      content: userMessage,
      timestamp: new Date()
    };
    setMessages([...messages, newUserMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Send message to API
      const response = await axios.post(`${API_BASE_URL}/chat`, {
        message: userMessage,
        session_id: sessionId
      }, {
        timeout: 120000 // 2 minute timeout
      });

      if (response.data.success) {
        const assistantMessage = {
          id: messages.length + 2,
          type: 'assistant',
          content: response.data.response,
          timestamp: new Date()
        };
        setMessages(prev => [...prev, assistantMessage]);
      } else {
        const errorMessage = {
          id: messages.length + 2,
          type: 'error',
          content: `Error: ${response.data.error}`,
          timestamp: new Date()
        };
        setMessages(prev => [...prev, errorMessage]);
      }
    } catch (error) {
      const errorMessage = {
        id: messages.length + 2,
        type: 'error',
        content: `Connection error: ${error.message}. Make sure the backend is running on http://localhost:5000`,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearHistory = async () => {
    try {
      await axios.delete(`${API_BASE_URL}/history/${sessionId}`);
      setMessages([
        {
          id: 1,
          type: 'assistant',
          content: '🗑️ Conversation cleared!\n\nLet\'s start fresh. Ask me anything!',
          timestamp: new Date()
        }
      ]);
    } catch (error) {
      console.error('Error clearing history:', error);
    }
  };

  return (
    <div className="app dark-theme">
      <Header onClearHistory={handleClearHistory} />
      <StatusBar status={apiStatus} />
      
      <div className="chat-container">
        <div className="messages">
          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          {isLoading && (
            <div className="message assistant-message">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      <InputBox 
        onSendMessage={handleSendMessage} 
        isLoading={isLoading}
        isConnected={apiStatus === 'connected'}
        inputValue={inputValue}
        setInputValue={setInputValue}
      />
    </div>
  );
}

export default App;
