import axios from "axios";

const documentApi = axios.create({
  baseURL: import.meta.env.VITE_DOCUMENT_SERVICE_URL || "http://localhost:8001/api/v1",
  headers: {
    Authorization: "Bearer mocked_token"
  }
});

export const uploadDocument = async (file: File) => {
  const formData = new FormData();
  formData.append("file", file);
  return documentApi.post("/documents", formData);
};

export const fetchDocuments = async () => {
  return documentApi.get("/documents").then((res) => res.data);
};
