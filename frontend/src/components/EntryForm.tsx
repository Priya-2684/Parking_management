import { useState } from "react";
import { vehicleEntryApi } from "../api/parkingApi";
import { validateIndianVehicleNumber, formatVehicleNumber } from "../utils/vehicleValidation";

export default function EntryForm() {
  const [vehicleNumber, setVehicleNumber] = useState("");
  const [vehicleType, setVehicleType] = useState("Bike");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleVehicleNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const formatted = formatVehicleNumber(e.target.value);
    setVehicleNumber(formatted);
    
    // Clear error when user starts typing
    if (error) setError("");
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Validate vehicle number
    const validation = validateIndianVehicleNumber(vehicleNumber);
    if (!validation.isValid) {
      setError(validation.message);
      return;
    }

    try {
      const res = await vehicleEntryApi({
        vehicle_number: vehicleNumber,
        vehicle_type: vehicleType,
      });

      setMessage(`Vehicle entered successfully. Slot assigned: ${res.slot_number} at ${new Date(res.entry_time).toLocaleString()}`);
      setVehicleNumber("");
      setVehicleType("Bike");
      setError("");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Vehicle entry failed");
      setMessage("");
    }
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
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

      <select value={vehicleType} onChange={(e) => setVehicleType(e.target.value)}>
        <option value="Bike">Bike</option>
        <option value="Car">Car</option>
      </select>

      <button className="btn" type="submit">
        Register Entry
      </button>

      {message && <p style={{ color: '#28a745' }}>{message}</p>}
    </form>
  );
}