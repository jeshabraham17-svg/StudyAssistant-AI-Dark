import React from 'react';
import { FiCheck } from 'react-icons/fi';

function ChatMessage({ message }) {
  const isUser = message.type === 'user';
  const isError = message.type === 'error';

  return (
    <div className={`message ${isUser ? 'user-message' : isError ? 'error-message' : 'assistant-message'}`}>
      <div className="message-avatar">
        {isUser ? '👤' : isError ? '⚠️' : '🤖'}
      </div>
      <div className="message-content">
        <p className="message-text">{message.content}</p>
        <span className="message-time">
          {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </span>
      </div>
    </div>
  );
}

export default ChatMessage;
