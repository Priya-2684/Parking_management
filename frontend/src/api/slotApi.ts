import axiosInstance from "./axiosInstance";
import type { Slot } from "../types/slot";

export const getSlotsApi = async (): Promise<Slot[]> => {
  const res = await axiosInstance.get("/slots");
  return res.data;
};

export const createSlotApi = async (data: {
  slot_number: string;
  slot_type: string;
}): Promise<Slot> => {
  const res = await axiosInstance.post("/slots", data);
  return res.data;
};