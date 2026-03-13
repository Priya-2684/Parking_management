import { Link } from "react-router-dom";
import { useAuth } from "../../hooks/useAuth";

export default function Sidebar() {
  const { user } = useAuth();

  return (
    <aside className="sidebar">
      <Link to="/dashboard" className="sidebar-link">Dashboard</Link>
      <Link to="/vehicle-entry" className="sidebar-link">Vehicle Entry</Link>
      <Link to="/vehicle-exit" className="sidebar-link">Vehicle Exit</Link>
      <Link to="/active-parking" className="sidebar-link">Active Parking</Link>
      <Link to="/parking-history" className="sidebar-link">Parking History</Link>

      {user?.role?.toLowerCase() === "admin" && (
        <>
          <Link to="/slot-management" className="sidebar-link">Add Slot</Link>
          <Link to="/pricing-management" className="sidebar-link">Pricing Management</Link>
          <Link to="/register" className="sidebar-link">Register Staff</Link>
        </>
      )}
    </aside>
  );
}