import axiosInstance from "./axiosInstance";
import type { User } from "../types/auth";

export const getCurrentUserApi = async (): Promise<User> => {
  const res = await axiosInstance.get("/users/me");
  return res.data;
};

export const getUsersApi = async (): Promise<User[]> => {
  const res = await axiosInstance.get("/users");
  return res.data;
};