import { create } from 'zustand';

interface ChatStore {
  selectedDocuments: string[];
  toggleDocument: (id: string) => void;
  activeConversationId: string | null;
  setActiveConversationId: (id: string | null) => void;
}

export const useChatStore = create<ChatStore>((set) => ({
  selectedDocuments: [],
  toggleDocument: (id) => set((state) => ({
    selectedDocuments: state.selectedDocuments.includes(id)
      ? state.selectedDocuments.filter(docId => docId !== id)
      : [...state.selectedDocuments, id]
  })),
  activeConversationId: null,
  setActiveConversationId: (id) => set({ activeConversationId: id }),
}));
