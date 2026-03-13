import axiosInstance from "./axiosInstance";
import type { Pricing } from "../types/pricing";

export const getPricingApi = async (): Promise<Pricing[]> => {
  const res = await axiosInstance.get("/pricing");
  return res.data;
};

export const savePricingApi = async (data: {
  vehicle_type: string;
  price_per_hour: number;
}): Promise<Pricing> => {
  const res = await axiosInstance.post("/pricing", data);
  return res.data;
};