import type { InfoToTransaction } from "../../types";
import { useEffect, useState } from "react";

type TransactionPropms = {
  infoTransaction: InfoToTransaction | null;
};
// falta recorrer infoTrasaction y pintarlo en el front , trae las trasacciones y ingresos y egeresos asi como el total
function TransactionPage({ infoTransaction }: TransactionPropms) {
  useEffect(() => {
    const fetchData = async () => {
      if (infoTransaction) {
        const accountData = await getTransactions(infoTransaction);
        console.log("MOSTRANDO TODAS LAS CUENTAS DATA ");
        console.log(accountData);
        setReturnAccount(accountData);
      }
    };

    fetchData();
  }, [infoBank]);

  return (
    <>
      <div>
        <div>Total</div>
        <div>
          <div>Ingresos</div>
          <div>Egresos</div>
        </div>
        <div className="p-4">
          <h1 className="text-xl font-bold mb-4">Bank</h1>
          <div className="overflow-x-auto">
            <table className="table-auto w-full border-collapse">
              <tbody>
                {Object.entries(infoReturnAccount ?? {}).map(
                  ([account_id, link]) => (
                    <tr
                      key={account_id}
                      onClick={() => handleAccountName(link[0], account_id)}
                      className="hover:bg-gray-100 cursor-pointer"
                    >
                      <td className="border px-4 py-2 text-center">
                        {link[1]}
                      </td>
                    </tr>
                  )
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
}
export default TransactionPage;
