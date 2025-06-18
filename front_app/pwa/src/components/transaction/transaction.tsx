import type { InfoToTransaction } from "../../types";
import { useEffect, useState } from "react";
import { getTransactions } from "../../utils/function";
import type { returnTransactions } from "../../types";

type TransactionPropms = {
  infoTransaction: InfoToTransaction | null;
};
// falta recorrer infoTrasaction y pintarlo en el front , trae las trasacciones y ingresos y egeresos asi como el total
function TransactionPage({ infoTransaction }: TransactionPropms) {
  const [infoReturnTransaction, setReturnTransaction] = useState<
    returnTransactions[] | null
  >(null);
  useEffect(() => {
    const fetchData = async () => {
      if (infoTransaction) {
        const transactionData = await getTransactions(infoTransaction);
        console.log(transactionData);
        if (
          transactionData.length === 2 &&
          Object.keys(transactionData[0]).length > 0 &&
          Object.keys(transactionData[1]).length > 0
        ) {
          setReturnTransaction(transactionData);
        }
      }
    };
    fetchData();
  }, [infoTransaction]);

  return (
    <>
      <div>
        {infoReturnTransaction && (
          <>
            <div>{infoReturnTransaction[1]["total"]}</div>
            <div>
              <div>{infoReturnTransaction[1]["ingreso"]}</div>
              <div>{infoReturnTransaction[1]["egreso"]}</div>
            </div>
          </>
        )}

        <div className="p-4">
          <h1 className="text-xl font-bold mb-4">Bank</h1>
          <div className="overflow-x-auto">
            <table className="table-auto w-full border-collapse">
              <tbody>
                {infoReturnTransaction &&
                  infoReturnTransaction.length > 0 &&
                  Object.entries(infoReturnTransaction[0]).map(
                    ([item, price]) => (
                      <tr
                        key={item}
                        className="hover:bg-gray-100 cursor-pointer"
                      >
                        <td className="border px-4 py-2 text-center">
                          {item} = {price}
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
