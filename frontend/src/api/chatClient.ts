import axios from "axios";

const chatApi = axios.create({
  baseURL: import.meta.env.VITE_CHAT_SERVICE_URL || "http://localhost:8002/api/v1",
  headers: {
    Authorization: "Bearer 00000000-0000-0000-0000-000000000000"
  }
});

export const createConversation = async (documentIds: string[]) => {
  return chatApi.post("/conversations", { document_ids: documentIds }).then(r => r.data);
};

export const getEventSourceUrl = (conversationId: string) => {
  return `${chatApi.defaults.baseURL}/conversations/${conversationId}/messages`;
};
