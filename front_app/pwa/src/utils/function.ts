import type { InfoBanks } from "../types";
import type { InfoToTransaction } from "../types";
async function getAccounts(infodata: InfoBanks) {
  console.log(infodata);
  const response = await fetch("http://localhost:5000/api/v1/accounts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(infodata),
  });

  const data = await response.json();
  return data.cuentas;
  console.log(data);
  console.log(data.statuscode);
}
export { getAccounts };

async function getTransactions(infoTransaction: InfoToTransaction) {
  const response = await fetch("http://localhost:5000/api/v1/transactions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(infoTransaction),
  });
  const data = await response.json();
  console.log(data);
  return data;
}
export { getTransactions };
