import { useState, useEffect } from "react";
import { getAccounts } from "../../utils/function";
import type { InfoBanks } from "../../types";
import type { returnAccounts } from "../../types";
import type { InfoToTransaction } from "../../types";
import { useNavigate } from "react-router-dom";

// interface InfoBanks {
//   institution: string;
//   email: string;
//   username_type: string;
//   password: string;
//   registered_link: string | "none";
// }
type AccountPageProps = {
  infoBank: InfoBanks | null;
  setInfoTransaction: React.Dispatch<
    React.SetStateAction<InfoToTransaction | null>
  >;
};

// const ned: InfoBanks = {
//   institution: "erebor_br_retail",
//   email: "ruizdani301@gmail.com",
//   username_type: "text",
//   password: "1234",
//   registered_link: "none",
// };{setInfoTRansaction}:setInfoTransaction
function AccountPage({ infoBank, setInfoTransaction }: AccountPageProps) {
  //   const [dataBank, setDataBank] = useState<Bank[]>([]);
  const [infoReturnAccount, setReturnAccount] = useState<returnAccounts | null>(
    null
  );

  const navigate = useNavigate();

  const handleAccountName = (id: string, link: string) => {
    setInfoTransaction({ id_account: id, link_account: link });
    alert(link);
    navigate("/transactions");
    // luego se redirecciona a la pagina de transacciones
  };

  useEffect(() => {
    const fetchData = async () => {
      if (infoBank) {
        const accountData = await getAccounts(infoBank);
        console.log("MOSTRANDO TODAS LAS CUENTAS DATA ");
        console.log(accountData);
        setReturnAccount(accountData);
      }
    };

    fetchData();
    // const response = getAccounts(ned);
    // setInfoAccount(response);
    // console.log("la respuesta");
    // console.log(response);
  }, [infoBank]);

  //   const handleAccountName = (id: string, link: string) => {
  //
  //   };

  return (
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
                  <td className="border px-4 py-2 text-center">{link[1]}</td>
                </tr>
              )
            )}{" "}
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default AccountPage;
