import React from 'react';
import { FiSend } from 'react-icons/fi';

function InputBox({ onSendMessage, isLoading, isConnected, inputValue, setInputValue }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      onSendMessage(inputValue);
    }
  };

  return (
    <form className="input-box" onSubmit={handleSubmit}>
      <input
        type="text"
        className="input-field"
        placeholder={isConnected ? "Ask anything about your studies..." : "🔴 Backend is offline. Start it first."}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        disabled={isLoading || !isConnected}
      />
      <button
        type="submit"
        className="send-btn"
        disabled={isLoading || !isConnected || !inputValue.trim()}
      >
        {isLoading ? '⏳' : <FiSend size={20} />}
      </button>
    </form>
  );
}

export default InputBox;
