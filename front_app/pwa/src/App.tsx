import { useState } from "react";

import BankPage from "./components/bank/bank";
function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <BankPage />
    </>
  );
}

export default App;
