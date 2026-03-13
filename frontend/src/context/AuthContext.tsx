import { createContext, useEffect, useState } from "react";
import { getCurrentUserApi } from "../api/userApi";
import type { User } from "../types/auth";
import { getToken, removeToken, setToken } from "../utils/token";

type AuthContextType = {
  user: User | null;
  token: string | null;
  loading: boolean;
  login: (token: string) => Promise<void>;
  logout: () => void;
};

export const AuthContext = createContext<AuthContextType>({
  user: null,
  token: null,
  loading: true,
  login: async () => {},
  logout: () => {},
});

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [tokenState, setTokenState] = useState<string | null>(getToken());
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const loadUser = async () => {
    try {
      const userData = await getCurrentUserApi();
      setUser(userData);
    } catch {
      logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (token: string) => {
    setToken(token);
    setTokenState(token);
    await loadUser();
  };

  const logout = () => {
    removeToken();
    setTokenState(null);
    setUser(null);
    setLoading(false);
  };

  useEffect(() => {
    if (tokenState) {
      loadUser();
    } else {
      setLoading(false);
    }
  }, [tokenState]);

  return (
    <AuthContext.Provider value={{ user, token: tokenState, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};