import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import ProtectedRoute from "../components/ProtectedRoute";
import PricingManagement from "../pages/PricingManagement";
import SlotManagement from "../pages/SlotManagement";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import NotFound from "../pages/NotFound";
import ActiveParking from "../pages/ActiveParking";
import ParkingHistory from "../pages/ParkingHistory";
import VehicleEntry from "../pages/VehicleEntry";
import VehicleExit from "../pages/VehicleExit";
import Register from "../pages/auth/Register";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />

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
        <Route
        path="/register"
      element={
      <ProtectedRoute>
        <Register />
      </ProtectedRoute>
  }
/>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}