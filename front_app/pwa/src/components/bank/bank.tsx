import { useState, useEffect } from "react";
import type { InfoBanks } from "../../types";
import { useNavigate } from "react-router-dom";

type BankPageProps = {
  setInfoBank: React.Dispatch<React.SetStateAction<InfoBanks | null>>;
};
interface Bank {
  id: string;
  name: string;
  display_name: string;
  icon_logo: string;
  country_code: string;
  username_type: string;
}
// interface InfoBanks {
//   institution: string;
//   email: string;
//   username_type: string;
//   password: string;
//   registered_link: string | "none";
// }

function BankPage({ setInfoBank }: BankPageProps) {
  const [dataBank, setDataBank] = useState<Bank[]>([]);
  const [email, setEmail] = useState<string>("");
  const [register_link, setRegisterLink] = useState<string | "none">("none");
  const navigate = useNavigate();
  useEffect(() => {
    fetch("http://localhost:5000/api/v1/banks")
      .then((response) => response.json())
      .then((data) => {
        setDataBank(data.all_banks);
      });
  }, []);

  const handleBankName = (bank: string, username_type: string) => {
    // email = localSrorage.getItem("email")
    // registered_link = localSrorage.getItem("registered_link")
    //if (registered_link != null){
    //  setRegisterLink(registered_link)
    //}
    const userInput = window.prompt(`Ingresa un número para el banco ${bank}:`);
    if (userInput !== null) {
      const pass = String(userInput);
      if (pass.length > 0) {
        alert(`ingresado: ${pass}`);
        const bankData: InfoBanks = {
          institution: bank,
          email: "ruizdani301@gmail.com",
          password: pass,
          username_type: username_type,
          registered_link: register_link ?? "none",
        };
        setInfoBank(bankData);
        navigate("/accounts");
      } else {
        alert("Por favor ingresa un valor valido");
      }
    }
  };
  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Bank</h1>
      <div className="overflow-x-auto">
        <table className="table-auto w-full border-collapse">
          <tbody>
            {dataBank.map((bank) => (
              <tr
                key={bank.id}
                onClick={() => handleBankName(bank.name, bank.username_type)}
                className="hover:bg-gray-100 cursor-pointer"
              >
                <td className="border px-4 py-2 text-center">
                  <img
                    src={bank.icon_logo}
                    alt={bank.display_name}
                    width="40"
                    className="mx-auto"
                  />
                </td>
                <td className="border px-4 py-2 text-sm md:text-base">
                  {bank.display_name}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default BankPage;
