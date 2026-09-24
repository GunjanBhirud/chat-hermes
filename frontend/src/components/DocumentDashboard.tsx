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

  if (isLoading) return <div>Loading documents...</div>;

  return (
    <div className="p-4 border-r border-gray-200 w-1/3">
      <h2 className="text-xl font-bold mb-4">Documents</h2>
      <div className="mb-4">
        <input 
          type="file" 
          ref={fileInputRef} 
          onChange={handleFileChange} 
          className="hidden" 
          accept=".pdf,.docx,.md"
        />
        <button 
          onClick={() => fileInputRef.current?.click()}
          className="px-4 py-2 bg-blue-600 text-white rounded cursor-pointer w-full text-center"
          disabled={uploadMutation.isPending}
        >
          {uploadMutation.isPending ? 'Uploading...' : 'Upload Document'}
        </button>
      </div>

      <ul className="space-y-2">
        {documents.map((doc: any) => (
          <li key={doc.document_id} className="flex items-center space-x-2 p-2 hover:bg-gray-50 rounded border">
            <input 
              type="checkbox" 
              checked={selectedDocuments.includes(doc.document_id)}
              onChange={() => toggleDocument(doc.document_id)}
              disabled={doc.status !== 'READY'}
              className="mt-1"
            />
            <div>
              <p className="font-semibold text-sm">{doc.name}</p>
              <p className="text-xs text-gray-500">{doc.status}</p>
            </div>
          </li>
        ))}
      </ul>
      {documents.length === 0 && <p className="text-sm text-gray-400">No documents yet.</p>}
    </div>
  );
};
