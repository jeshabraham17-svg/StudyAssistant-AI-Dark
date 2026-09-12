import React from 'react';
import { FiTrash2, FiSettings } from 'react-icons/fi';

function Header({ onClearHistory }) {
  return (
    <header className="header">
      <div className="header-content">
        <div className="header-left">
          <h1 className="header-title">📚 StudyAssistant AI</h1>
          <p className="header-subtitle">Privacy-Focused Educational Assistant</p>
        </div>
        <div className="header-right">
          <button 
            className="header-btn"
            title="Settings"
          >
            <FiSettings size={20} />
          </button>
          <button 
            className="header-btn danger"
            onClick={onClearHistory}
            title="Clear Conversation"
          >
            <FiTrash2 size={20} />
          </button>
        </div>
      </div>
    </header>
  );
}

export default Header;
