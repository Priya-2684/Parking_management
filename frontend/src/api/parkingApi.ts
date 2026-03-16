import axiosInstance from "./axiosInstance";
import type { ParkingRecord } from "../types/parking";

export const vehicleEntryApi = async (data: {
  vehicle_number: string;
  vehicle_type: string;
}): Promise<{
  message: string;
  vehicle_number: string;
  vehicle_type: string;
  slot_number: string;
  entry_time: string;
}> => {
  const res = await axiosInstance.post("/parking/entry", data);
  return res.data;
};

export const vehicleExitApi = async (data: {
  vehicle_number: string;
}): Promise<{
  message: string;
  vehicle_number: string;
  slot_number: string;
  duration_hours: number;
  charge: number;
  entry_time: string;
  exit_time: string;
}> => {
  const res = await axiosInstance.post("/parking/exit", data);
  return res.data;
};

export const getActiveParkingApi = async (): Promise<ParkingRecord[]> => {
  const res = await axiosInstance.get("/parking/active");
  return res.data;
};

export const getParkingHistoryApi = async (): Promise<ParkingRecord[]> => {
  const res = await axiosInstance.get("/parking/history");
  return res.data;
};