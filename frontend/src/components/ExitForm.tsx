import { useState, useEffect } from "react";
import { vehicleExitApi, getActiveParkingApi } from "../api/parkingApi";
import { validateIndianVehicleNumber, formatVehicleNumber } from "../utils/vehicleValidation";

export default function ExitForm() {
  const [vehicleNumber, setVehicleNumber] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [activeVehicles, setActiveVehicles] = useState<any[]>([]);
  const [useDropdown, setUseDropdown] = useState(false);

  const loadActiveVehicles = async () => {
    try {
      const vehicles = await getActiveParkingApi();
      setActiveVehicles(vehicles);
    } catch (err) {
      console.error("Failed to load active vehicles:", err);
    }
  };

  useEffect(() => {
    loadActiveVehicles();
  }, []);

  const handleVehicleNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const formatted = formatVehicleNumber(e.target.value);
    setVehicleNumber(formatted);
    
    // Clear error when user starts typing
    if (error) setError("");
  };

  const handleVehicleSelect = (selectedVehicleNumber: string) => {
    setVehicleNumber(selectedVehicleNumber);
    setUseDropdown(true);
    if (error) setError("");
  };

  const handleExit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Validate vehicle number
    const validation = validateIndianVehicleNumber(vehicleNumber);
    if (!validation.isValid) {
      setError(validation.message);
      return;
    }

    try {
      const res = await vehicleExitApi({
        vehicle_number: vehicleNumber,
      });

      setMessage(
        `Exit successful. Slot: ${res.slot_number}, Duration: ${res.duration_hours} hr(s), Charge: ₹${res.charge}\nEntry: ${new Date(res.entry_time).toLocaleString()}\nExit: ${new Date(res.exit_time).toLocaleString()}`
      );
      setVehicleNumber("");
      setError("");
      setUseDropdown(false);
      
      // Reload active vehicles
      loadActiveVehicles();
    } catch (err: any) {
      setError(err.response?.data?.detail || "Vehicle exit failed");
      setMessage("");
    }
  };

  return (
    <form className="card" onSubmit={handleExit}>
      <div style={{ marginBottom: "20px" }}>
        <label style={{ display: "block", marginBottom: "10px", fontWeight: "bold" }}>
          Exit Method:
        </label>
        <div style={{ display: "flex", gap: "15px", marginBottom: "15px" }}>
          <label>
            <input
              type="radio"
              name="exitMethod"
              checked={!useDropdown}
              onChange={() => setUseDropdown(false)}
              style={{ marginRight: "5px" }}
            />
            Manual Entry
          </label>
          <label>
            <input
              type="radio"
              name="exitMethod"
              checked={useDropdown}
              onChange={() => setUseDropdown(true)}
              style={{ marginRight: "5px" }}
            />
            Quick Select
          </label>
        </div>
      </div>

      {useDropdown && activeVehicles.length > 0 ? (
        <div>
          <label style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>
            Select Parked Vehicle:
          </label>
          <select
            value={vehicleNumber}
            onChange={(e) => handleVehicleSelect(e.target.value)}
            required
            style={{ 
              width: "100%", 
              padding: "10px", 
              marginBottom: "15px",
              borderColor: error ? '#ff4444' : '#ccc'
            }}
          >
            <option value="">Choose a vehicle...</option>
            {activeVehicles.map((vehicle) => (
              <option key={vehicle.id} value={vehicle.vehicle_number}>
                {vehicle.vehicle_number} - Slot {vehicle.slot_number} ({vehicle.vehicle_type}) - 
                Entered: {new Date(vehicle.entry_time).toLocaleString()}
              </option>
            ))}
          </select>
          {error && <p style={{ color: '#ff4444', fontSize: '12px', margin: '0 0 15px 0' }}>{error}</p>}
        </div>
      ) : (
        <div>
          <input
            type="text"
            placeholder="Vehicle Number (AB12CD3456)"
            value={vehicleNumber}
            onChange={handleVehicleNumberChange}
            required
            style={{ 
              borderColor: error ? '#ff4444' : '#ccc',
              marginBottom: error ? '5px' : '15px'
            }}
          />
          {error && <p style={{ color: '#ff4444', fontSize: '12px', margin: '0 0 15px 0' }}>{error}</p>}
        </div>
      )}

      {useDropdown && activeVehicles.length === 0 && (
        <div style={{ 
          padding: "10px", 
          backgroundColor: "#fff3cd", 
          border: "1px solid #ffeaa7", 
          borderRadius: "4px", 
          marginBottom: "15px" 
        }}>
          No vehicles currently parked. Use manual entry or check back later.
        </div>
      )}

      <button className="btn danger" type="submit" disabled={!vehicleNumber}>
        Exit Vehicle
      </button>

      {message && (
        <p style={{ 
          color: '#28a745', 
          whiteSpace: 'pre-line',
          marginTop: '15px',
          padding: '10px',
          backgroundColor: '#d4edda',
          border: '1px solid #c3e6cb',
          borderRadius: '4px'
        }}>
          {message}
        </p>
      )}
    </form>
  );
}