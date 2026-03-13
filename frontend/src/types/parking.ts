export type ParkingRecord = {
  id: number;
  vehicle_number: string;
  vehicle_type: string;
  slot_number: string;
  entry_time: string;
  exit_time: string | null;
  duration_hours: number | null;
  charge: number | null;
  status: string;
};