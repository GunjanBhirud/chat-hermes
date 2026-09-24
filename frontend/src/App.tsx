import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { DocumentDashboard } from './components/DocumentDashboard';
import { ChatContainer } from './components/ChatContainer';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="flex h-screen bg-white text-gray-900 font-sans">
        <DocumentDashboard />
        <ChatContainer />
      </div>
    </QueryClientProvider>
  );
}

export default App;
