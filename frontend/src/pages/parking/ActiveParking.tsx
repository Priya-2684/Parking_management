import { useEffect, useState } from "react";
import { getActiveParkingApi } from "../../api/parkingApi";
import ParkingTable from "../../components/parking/ParkingTable";
import DashboardLayout from "../../layouts/DashboardLayout";
import type { ParkingRecord } from "../../types/parking";

export default function ActiveParking() {
  const [data, setData] = useState<ParkingRecord[]>([]);

  const loadData = async () => {
    const res = await getActiveParkingApi();
    setData(res);
  };

  useEffect(() => {
    loadData();
  }, []);

  return (
    <DashboardLayout>
      <h2>Active Parking</h2>
      <ParkingTable data={data} />
    </DashboardLayout>
  );
}