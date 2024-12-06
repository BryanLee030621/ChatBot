import React from 'react';
import FileUpload from './components/FileUpload';
import ChatWindow from './components/ChatWindow';

function App() {
  return (
    <div>
      <h1>Chatbot with BERT and GPT</h1>
      <FileUpload />
      <ChatWindow />
    </div>
  );
}

export default App;
