import React, { useState, useEffect, useRef } from 'react';
import { useMutation } from '@tanstack/react-query';
import { createConversation, getEventSourceUrl } from '../api/chatClient';
import { useChatStore } from '../store/chatStore';

export const ChatContainer: React.FC = () => {
  const { selectedDocuments, activeConversationId, setActiveConversationId } = useChatStore();
  const [messages, setMessages] = useState<{role: string, content: string, sources?: any[]}[]>([]);
  const [input, setInput] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  
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

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isStreaming]);

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
        "Authorization": "Bearer 00000000-0000-0000-0000-000000000000"
      },
      body: JSON.stringify({ content: input })
    }).then(async response => {
      setInput('');
      
      if (!response.ok) {
         try {
             const errorData = await response.json();
             setMessages(prev => [...prev, { role: 'assistant', content: 'Connection Error: ' + (errorData.detail || 'Service unavailable') }]);
         } catch {
             setMessages(prev => [...prev, { role: 'assistant', content: 'Connection Error: Failed to reach the service.' }]);
         }
         setIsStreaming(false);
         return;
      }

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
              } else if (data.chunk_id) {
                assistantMsg.sources?.push(data);
              }
              // update locally
              setMessages(prev => {
                const newMsgs = [...prev];
                newMsgs[newMsgs.length - 1] = { ...assistantMsg };
                return newMsgs;
              });
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
      <div className="flex-1 flex flex-col items-center justify-center bg-slate-50 relative overflow-hidden">
        <div className="absolute inset-0 opacity-5 pointer-events-none bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-900 via-transparent to-transparent"></div>
        <div className="text-center p-10 bg-white/70 backdrop-blur shadow-2xl rounded-2xl border border-white max-w-md transform transition-all hover:scale-105 duration-300 z-10">
          <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-6 shadow-inner">
            <svg className="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
          </div>
          <h2 className="text-2xl font-extrabold mb-3 text-slate-800">Start a Conversation</h2>
          <p className="mb-8 text-slate-500">Select one or more <span className="font-semibold text-green-600">READY</span> documents from your library to provide context.</p>
          <button 
            onClick={startChat}
            disabled={selectedDocuments.length === 0 || createConvMutation.isPending}
            className="w-full px-6 py-3.5 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-medium rounded-xl shadow-lg shadow-blue-200 transition-all hover:shadow-xl hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:scale-100"
          >
            {createConvMutation.isPending ? 'Connecting...' : 'Begin Chat Session'}
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 flex flex-col bg-slate-50 relative">
      <div className="p-5 border-b border-slate-200 bg-white/80 backdrop-blur sticky top-0 z-10 shadow-sm flex items-center justify-between">
        <h2 className="font-bold text-slate-800 flex items-center gap-2">
          <span className="w-2.5 h-2.5 bg-green-500 rounded-full animate-pulse"></span>
          Active Chat Session
        </h2>
        <div className="text-xs font-semibold text-slate-500 bg-slate-100 px-3 py-1 rounded-full border border-slate-200 shadow-sm">
          {selectedDocuments.length} doc(s) scoped
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-6 space-y-6 z-0" style={{ scrollBehavior: 'smooth' }}>
        {messages.length === 0 && (
          <div className="text-center text-slate-400 mt-10 transition-opacity duration-500">
            <p className="inline-block px-4 py-2 bg-slate-200/50 rounded-full text-sm shadow-sm backdrop-blur">Ask anything about the selected documents!</p>
          </div>
        )}
        
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'} animate-[slideUp_0.3s_ease-out]`}>
            <div className={`p-4 rounded-2xl max-w-[80%] shadow-sm ${m.role === 'user' ? 'bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-br-sm' : 'bg-white border border-slate-100 text-slate-800 rounded-bl-sm shadow-md'}`}>
              <p className="whitespace-pre-wrap leading-relaxed">{m.content}</p>
              
              {m.sources && m.sources.length > 0 && (
                <div className="mt-3 pt-3 border-t border-slate-200/50 text-xs opacity-80 flex flex-wrap gap-2">
                  <span className="font-medium mr-1 text-slate-500">Sources:</span>
                  {m.sources.map((s, idx) => (
                    <span key={idx} className="bg-slate-100/80 px-2 py-0.5 rounded cursor-pointer hover:bg-slate-200 transition-colors border border-slate-200">
                      {s.source_id}
                    </span>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
        {isStreaming && (
          <div className="flex justify-start opacity-70 transition-opacity duration-300">
            <div className="p-4 rounded-2xl bg-white border border-slate-100 text-slate-800 rounded-bl-sm shadow-sm flex items-center gap-1.5 h-12">
              <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></span>
              <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce [animation-delay:0.2s]"></span>
              <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce [animation-delay:0.4s]"></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="p-6 border-t border-slate-200 bg-white z-10 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
        <div className="flex items-center bg-slate-50 p-2 rounded-2xl border border-slate-200 focus-within:ring-2 focus-within:ring-blue-500 focus-within:bg-white transition-all shadow-inner relative">
          <input 
            type="text"
            className="flex-1 bg-transparent border-none focus:outline-none p-3 text-slate-800 placeholder-slate-400"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSend()}
            placeholder="Ask a question about the reference docs..."
          />
          <button 
            onClick={handleSend}
            disabled={isStreaming || !input.trim()}
            className="p-3.5 bg-blue-600 text-white rounded-xl disabled:bg-slate-200 disabled:text-slate-400 transition-all hover:bg-blue-700 mx-1 flex items-center justify-center shadow-md active:scale-95 disabled:shadow-none"
          >
            <svg className="w-5 h-5 translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
          </button>
        </div>
      </div>
    </div>
  );
};
