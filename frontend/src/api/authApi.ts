import axiosInstance from "./axiosInstance";
import type { LoginResponse } from "../types/auth";

export const registerApi = async (data: {
  username: string;
  email: string;
  password: string;
  role: string;
}) => {
  const res = await axiosInstance.post("/auth/register", data);
  return res.data;
};

export const loginApi = async (data: {
  username: string;
  password: string;
}): Promise<LoginResponse> => {
  const res = await axiosInstance.post("/auth/login", data);
  return res.data;
};