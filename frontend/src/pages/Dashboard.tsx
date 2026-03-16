import { useEffect, useState } from "react";
import axios from "axios";
import DashboardCards from "../components/DashboardCards";
import DashboardLayout from "../layouts/DashboardLayout";
import { useAuth } from "../hooks/useAuth";

type DashboardStats = {
  total_slots: number;
  occupied_slots: number;
  available_slots: number;
  today_entries: number;
  today_exits: number;
  active_vehicles: number;
};

export default function Dashboard() {
  const { user } = useAuth();

  const [stats, setStats] = useState<DashboardStats>({
    total_slots: 0,
    occupied_slots: 0,
    available_slots: 0,
    today_entries: 0,
    today_exits: 0,
    active_vehicles: 0,
  });

  const fetchDashboardStats = async () => {
    try {
      const token = localStorage.getItem("token");

      const response = await axios.get("http://127.0.0.1:8000/dashboard/stats", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setStats(response.data);
    } catch (error) {
      console.error("Error fetching dashboard stats:", error);
    }
  };

  useEffect(() => {
    fetchDashboardStats();
  }, []);

  return (
    <DashboardLayout>
      <div className="card">
        <h2>Dashboard</h2>
        <p>Welcome, {user?.username}</p>
        <p>Role: {user?.role}</p>
      </div>

      <div className="slot-grid">
        <DashboardCards title="Total Slots" value={stats.total_slots} />
        <DashboardCards title="Occupied Slots" value={stats.occupied_slots} />
        <DashboardCards title="Available Slots" value={stats.available_slots} />
        <DashboardCards title="Today Entries" value={stats.today_entries} />
        <DashboardCards title="Today Exits" value={stats.today_exits} />
        <DashboardCards title="Active Vehicles" value={stats.active_vehicles} />
      </div>
    </DashboardLayout>
  );
}