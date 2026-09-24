import React, { useState, useEffect, useRef } from 'react';
import { useMutation } from '@tanstack/react-query';
import { createConversation, getEventSourceUrl } from '../api/chatClient';
import { useChatStore } from '../store/chatStore';

export const ChatContainer: React.FC = () => {
  const { selectedDocuments, activeConversationId, setActiveConversationId } = useChatStore();
  const [messages, setMessages] = useState<{role: string, content: string, sources?: any[]}[]>([]);
  const [input, setInput] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  
  const createConvMutation = useMutation({
    mutationFn: () => createConversation(selectedDocuments),
    onSuccess: (data) => {
      setActiveConversationId(data.conversation_id);
      setMessages([]);
    }
  });

  const startChat = () => {
    if (selectedDocuments.length > 0) {
      createConvMutation.mutate();
    }
  };

  const handleSend = () => {
    if (!input.trim() || !activeConversationId || isStreaming) return;

    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setIsStreaming(true);

    const sseUrl = getEventSourceUrl(activeConversationId);
    
    fetch(sseUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer mocked_token"
      },
      body: JSON.stringify({ content: input })
    }).then(async response => {
      setInput('');
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      
      let assistantMsg = { role: 'assistant', content: '', sources: [] };
      setMessages(prev => [...prev, assistantMsg]);
      
      if (!reader) return;
      
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split('\n');
        
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6));
              if (data.text) {
                assistantMsg.content += data.text;
                // update last message
                setMessages(prev => {
                  const newMsgs = [...prev];
                  newMsgs[newMsgs.length - 1] = { ...assistantMsg };
                  return newMsgs;
                });
              }
            } catch (e) {}
          }
        }
      }
      setIsStreaming(false);
    }).catch(() => {
      setIsStreaming(false);
    });
  };

  if (!activeConversationId) {
    return (
      <div className="flex-1 flex items-center justify-center bg-gray-50">
        <div className="text-center p-8 bg-white shadow rounded">
          <h2 className="text-xl font-bold mb-4">Start a Conversation</h2>
          <p className="mb-4 text-gray-600">Select one or more READY documents from the sidebar.</p>
          <button 
            onClick={startChat}
            disabled={selectedDocuments.length === 0 || createConvMutation.isPending}
            className="px-6 py-2 bg-blue-600 text-white rounded cursor-pointer disabled:bg-gray-400"
          >
            {createConvMutation.isPending ? 'Starting...' : 'Start Chat'}
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 flex flex-col">
      <div className="p-4 border-b">
        <h2 className="font-bold">Active Chat</h2>
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((m, i) => (
          <div key={i} className={`p-3 rounded-lg max-w-[80%] ${m.role === 'user' ? 'bg-blue-100 ml-auto' : 'bg-gray-100'}`}>
            <p className="whitespace-pre-wrap">{m.content}</p>
          </div>
        ))}
        {isStreaming && <div className="text-gray-400 text-sm">Assistant is typing...</div>}
      </div>
      <div className="p-4 border-t">
        <div className="flex space-x-2">
          <input 
            type="text"
            className="flex-1 border rounded p-2"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSend()}
            placeholder="Ask about your documents..."
          />
          <button 
            onClick={handleSend}
            disabled={isStreaming || !input.trim()}
            className="px-4 py-2 bg-blue-600 text-white rounded disabled:bg-gray-400"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};
