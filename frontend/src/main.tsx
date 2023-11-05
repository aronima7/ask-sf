import { createRoot } from "react-dom/client";
// import Chat from "./ChatApp";
import { Chat } from "./app";
// import { ChartView } from "./chart-view";
// import { ChartsView } from "./charts-view";
import { BrowserRouter, Route, Routes } from "react-router-dom";

const container = document.getElementById("root");
const root = createRoot(container!);
// const isLocalhost = window.location.hostname === "localhost";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* <Route path="/chart" element={<ChartView />} />
        <Route path="/charts" element={<ChartsView />} /> */}
        <Route path="/" element={<Chat />} />
      </Routes>
    </BrowserRouter>
  );
};

root.render(<App />);
