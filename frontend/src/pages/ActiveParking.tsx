import { useEffect, useState } from "react";
import { getActiveParkingApi, vehicleExitApi } from "../api/parkingApi";
import ParkingTable from "../components/ParkingTable";
import DashboardLayout from "../layouts/DashboardLayout";
import type { ParkingRecord } from "../types/parking";

export default function ActiveParking() {
  const [data, setData] = useState<ParkingRecord[]>([]);
  const [message, setMessage] = useState("");

  const loadData = async () => {
    const res = await getActiveParkingApi();
    setData(res);
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleQuickExit = async (vehicleNumber: string, slotNumber: string) => {
    try {
      const res = await vehicleExitApi({
        vehicle_number: vehicleNumber,
      });

      setMessage(
        `Vehicle ${vehicleNumber} exited successfully from slot ${slotNumber}. Duration: ${res.duration_hours} hr(s), Charge: ₹${res.charge}`
      );
      
      // Reload the active vehicles list
      loadData();
      
      // Clear message after 5 seconds
      setTimeout(() => setMessage(""), 5000);
    } catch (err: any) {
      setMessage(`Failed to exit vehicle: ${err.response?.data?.detail || "Unknown error"}`);
      setTimeout(() => setMessage(""), 5000);
    }
  };

  return (
    <DashboardLayout>
      <h2>Active Parking</h2>
      
      {message && (
        <div style={{
          padding: "10px",
          marginBottom: "20px",
          backgroundColor: message.includes("success") ? "#d4edda" : "#f8d7da",
          border: `1px solid ${message.includes("success") ? "#c3e6cb" : "#f5c6cb"}`,
          borderRadius: "4px",
          color: message.includes("success") ? "#155724" : "#721c24"
        }}>
          {message}
        </div>
      )}

      <ParkingTable data={data} onQuickExit={handleQuickExit} />
    </DashboardLayout>
  );
}