export type User = {
  id: number;
  username: string;
  email: string;
  role: string;
};

export type LoginResponse = {
  access_token: string;
  token_type: string;
};