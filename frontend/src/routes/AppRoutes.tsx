import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import ProtectedRoute from "../components/common/ProtectedRoute";
import PricingManagement from "../pages/admin/PricingManagement";
import SlotManagement from "../pages/admin/SlotManagement";
import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Dashboard from "../pages/dashboard/Dashboard";
import NotFound from "../pages/NotFound";
import ActiveParking from "../pages/parking/ActiveParking";
import ParkingHistory from "../pages/parking/ParkingHistory";
import VehicleEntry from "../pages/parking/VehicleEntry";
import VehicleExit from "../pages/parking/VehicleExit";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />

        <Route
          path="/register"
          element={
            <ProtectedRoute>
              <Register />
            </ProtectedRoute>
          }
        />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/vehicle-entry"
          element={
            <ProtectedRoute>
              <VehicleEntry />
            </ProtectedRoute>
          }
        />

        <Route
          path="/vehicle-exit"
          element={
            <ProtectedRoute>
              <VehicleExit />
            </ProtectedRoute>
          }
        />

        <Route
          path="/active-parking"
          element={
            <ProtectedRoute>
              <ActiveParking />
            </ProtectedRoute>
          }
        />

        <Route
          path="/parking-history"
          element={
            <ProtectedRoute>
              <ParkingHistory />
            </ProtectedRoute>
          }
        />

        <Route
          path="/slot-management"
          element={
            <ProtectedRoute>
              <SlotManagement />
            </ProtectedRoute>
          }
        />

        <Route
          path="/pricing-management"
          element={
            <ProtectedRoute>
              <PricingManagement />
            </ProtectedRoute>
          }
        />

        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}