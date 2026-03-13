import { useState } from "react";
import { vehicleEntryApi } from "../../api/parkingApi";

export default function EntryForm() {
  const [vehicleNumber, setVehicleNumber] = useState("");
  const [vehicleType, setVehicleType] = useState("Bike");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const res = await vehicleEntryApi({
        vehicle_number: vehicleNumber,
        vehicle_type: vehicleType,
      });

      setMessage(`Vehicle entered successfully. Slot assigned: ${res.slot_number}`);
      setVehicleNumber("");
      setVehicleType("Bike");
    } catch (err: any) {
      setMessage(err.response?.data?.detail || "Vehicle entry failed");
    }
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Vehicle Number"
        value={vehicleNumber}
        onChange={(e) => setVehicleNumber(e.target.value)}
        required
      />

      <select value={vehicleType} onChange={(e) => setVehicleType(e.target.value)}>
        <option value="Bike">Bike</option>
        <option value="Car">Car</option>
      </select>

      <button className="btn" type="submit">
        Register Entry
      </button>

      {message && <p>{message}</p>}
    </form>
  );
}