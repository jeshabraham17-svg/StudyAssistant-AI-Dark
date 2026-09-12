import React from 'react';

function StatusBar({ status }) {
  const statusConfig = {
    connected: { color: 'bg-green-600', text: '🟢 Connected to AI' },
    disconnected: { color: 'bg-red-600', text: '🔴 Backend offline' },
    checking: { color: 'bg-yellow-600', text: '🟡 Checking connection...' }
  };

  const config = statusConfig[status] || statusConfig.checking;

  return (
    <div className={`status-bar ${config.color}`}>
      {config.text}
    </div>
  );
}

export default StatusBar;
