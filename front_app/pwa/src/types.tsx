interface InfoBanks {
  institution: string;
  email: string;
  username_type: string;
  password: string;
  registered_link: string | "none";
}

export type { InfoBanks };

interface InfoToTransaction {
  id_account: string;
  link_account: string;
}

export type { InfoToTransaction };

interface returnAccounts {
  [key: string]: [string, string];
}
export type { returnAccounts };
