import React, { useRef } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { fetchDocuments, uploadDocument } from '../api/documentClient';
import { useChatStore } from '../store/chatStore';

export const DocumentDashboard: React.FC = () => {
  const queryClient = useQueryClient();
  const fileInputRef = useRef<HTMLInputElement>(null);
  const { selectedDocuments, toggleDocument } = useChatStore();

  const { data: documents = [], isLoading } = useQuery({
    queryKey: ['documents'],
    queryFn: fetchDocuments,
    refetchInterval: 5000 // Poll status every 5 seconds
  });

  const uploadMutation = useMutation({
    mutationFn: uploadDocument,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['documents'] });
    }
  });

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      uploadMutation.mutate(e.target.files[0]);
      e.target.value = '';
    }
  };

  return (
    <div className="w-1/3 bg-slate-50 border-r border-slate-200 p-6 flex flex-col shadow-inner">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600 drop-shadow-sm">Hermes Library</h2>
      </div>

      <div className="mb-6">
        <input 
          type="file" 
          ref={fileInputRef} 
          onChange={handleFileChange} 
          className="hidden" 
          accept=".pdf,.docx,.md"
        />
        <button 
          onClick={() => fileInputRef.current?.click()}
          className="flex justify-center items-center w-full px-4 py-3 bg-gradient-to-r from-indigo-500 to-blue-600 text-white rounded-xl shadow cursor-pointer transition-all hover:scale-[1.02] hover:shadow-md active:scale-95 font-medium disabled:opacity-70 disabled:scale-100"
          disabled={uploadMutation.isPending}
        >
          {uploadMutation.isPending ? (
            <span className="flex items-center gap-2">
              <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              Uploading...
            </span>
          ) : 'Upload Document'}
        </button>
      </div>

      <div className="flex-1 overflow-y-auto">
        {isLoading ? (
          <div className="animate-pulse space-y-4">
            {[1, 2, 3].map(i => (
              <div key={i} className="h-16 bg-slate-200 rounded-lg"></div>
            ))}
          </div>
        ) : (
          <ul className="space-y-3">
            {documents.length === 0 ? (
              <li className="text-sm text-slate-400 text-center mt-10">No documents yet.</li>
            ) : (
              documents.map((doc: any) => (
                <li 
                  key={doc.document_id} 
                  onClick={() => doc.status === 'READY' && toggleDocument(doc.document_id)}
                  className={`flex items-center gap-3 p-3 rounded-lg border transition-all duration-200 cursor-pointer shadow-sm
                    ${selectedDocuments.includes(doc.document_id) 
                      ? 'bg-blue-50 border-blue-200 ring-1 ring-blue-500 shadow-md transform -translate-y-0.5' 
                      : 'bg-white border-slate-200 hover:border-blue-300 hover:bg-slate-50'
                    }
                    ${doc.status !== 'READY' && 'opacity-60 cursor-not-allowed grayscale'}`
                  }
                >
                  <div className="flex-shrink-0">
                    <input 
                      type="checkbox" 
                      checked={selectedDocuments.includes(doc.document_id)}
                      readOnly
                      className="w-4 h-4 text-blue-600 rounded focus:ring-blue-500 cursor-pointer disabled:cursor-not-allowed"
                    />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-semibold text-sm text-slate-800 truncate">{doc.name}</p>
                    <p className="text-xs font-medium tracking-wide text-slate-500 uppercase flex items-center gap-1">
                      {doc.status === 'PROCESSING' || doc.status === 'QUEUED' ? (
                        <span className="flex items-center gap-1.5"><span className="w-1.5 h-1.5 bg-amber-400 rounded-full animate-pulse"></span> {doc.status}</span>
                      ) : doc.status === 'FAILED' ? (
                        <span className="flex items-center gap-1.5 text-red-500"><span className="w-1.5 h-1.5 bg-red-500 rounded-full"></span> {doc.status}</span>
                      ) : (
                        <span className="flex items-center gap-1.5 text-green-600"><span className="w-1.5 h-1.5 bg-green-500 rounded-full"></span> {doc.status}</span>
                      )}
                    </p>
                  </div>
                </li>
              ))
            )}
          </ul>
        )}
      </div>
    </div>
  );
};
