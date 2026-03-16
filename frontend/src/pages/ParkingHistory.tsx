import { useEffect, useState } from "react";
import { getParkingHistoryApi } from "../api/parkingApi";
import ParkingTable from "../components/ParkingTable";
import DashboardLayout from "../layouts/DashboardLayout";
import type { ParkingRecord } from "../types/parking";

export default function ParkingHistory() {
  const [data, setData] = useState<ParkingRecord[]>([]);

  const loadData = async () => {
    const res = await getParkingHistoryApi();
    setData(res);
  };

  useEffect(() => {
    loadData();
  }, []);

  return (
    <DashboardLayout>
      <h2>Parking History</h2>
      <ParkingTable data={data} />
    </DashboardLayout>
  );
}