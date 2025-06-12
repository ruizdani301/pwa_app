import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import BankPage from "./components/bank/bank";
import AccountPage from "./components/accounts/account";
import TransactionPage from "./components/transaction/transaction";
import type { InfoBanks } from "./types";
import type { InfoToTransaction } from "./types";

function App() {
  const [infoBank, setInfoBank] = useState<InfoBanks | null>(null);
  const [infoTransaction, setInfoTransaction] =
    useState<InfoToTransaction | null>(null);

  return (
    <Router>
      <Routes>
        <Route path="/banks" element={<BankPage setInfoBank={setInfoBank} />} />
        <Route
          path="/accounts"
          element={
            <AccountPage
              infoBank={infoBank}
              setInfoTransaction={setInfoTransaction}
            />
          }
        />
      </Routes>
      <Route
        path="/transactions"
        element={<TransactionPage infoTransaction={infoTransaction} />}
      ></Route>
    </Router>
  );
}

export default App;
