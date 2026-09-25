import axios from "axios";

const documentApi = axios.create({
  baseURL: import.meta.env.VITE_DOCUMENT_SERVICE_URL || "http://localhost:8001/api/v1",
  headers: {
    Authorization: "Bearer 00000000-0000-0000-0000-000000000000"
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
