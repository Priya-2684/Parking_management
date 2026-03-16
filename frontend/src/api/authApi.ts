import axiosInstance from "./axiosInstance";
import type { LoginResponse } from "../types/auth";

export const registerApi = async (data: {
  username: string;
  email: string;
  password: string;
  role: string;
}) => {
  console.log("Attempting registration to:", "/auth/register", "with data:", { 
    username: data.username, 
    email: data.email, 
    role: data.role 
  });
  try {
    const res = await axiosInstance.post("/auth/register", data);
    console.log("Registration response:", res.data);
    return res.data;
  } catch (error: any) {
    console.error("Registration API error:", error.response?.data || error.message);
    throw error;
  }
};

export const loginApi = async (data: {
  username: string;
  password: string;
}): Promise<LoginResponse> => {
  console.log("Attempting login to:", "/auth/login", "with data:", { username: data.username });
  try {
    const res = await axiosInstance.post("/auth/login", data);
    console.log("Login response:", res.data);
    return res.data;
  } catch (error: any) {
    console.error("Login API error:", error.response?.data || error.message);
    throw error;
  }
};