import { useState, useEffect } from "react";
import "./bank.css";

// interface Bank {
//   id: string;
//   name: string;
//   display_name: string;
//   icon_logo: string;
//   country_code: string;
//   username_type: string;
// }
// interface InfoBanks {
//   institution: string;
//   name: string;
//   username_type: string;
//   password: string;
//   registered_link: string | "none";
// }

function AccountPage() {
  //   const [dataBank, setDataBank] = useState<Bank[]>([]);
  //   const [infoBank, setInfoBank] = useState<InfoBanks | null>(null);

  //   useEffect(() => {
  //     fetch("http://localhost:5000/api/v1/banks")
  //       .then((response) => response.json())
  //       .then((data) => {
  //         setDataBank(data.all_banks);
  //       });
  //   }, []);

  const handleAccountName = (bank: string) => {
    const userInput = window.prompt(`Ingresa un número para el banco ${bank}:`);
    if (userInput !== null) {
      const num = Number(userInput);
      if (!isNaN(num)) {
        alert(`Número ingresado: ${num}`);
      } else {
        alert("Por favor ingresa un número válido");
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
                onClick={() => handleAccountName(bank.name)}
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
export default AccountPage;
