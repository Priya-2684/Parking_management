import { useState } from "react";
import { vehicleExitApi } from "../../api/parkingApi";

export default function ExitForm() {
  const [vehicleNumber, setVehicleNumber] = useState("");
  const [message, setMessage] = useState("");

  const handleExit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const res = await vehicleExitApi({
        vehicle_number: vehicleNumber,
      });

      setMessage(
        `Exit successful. Slot: ${res.slot_number}, Duration: ${res.duration_hours} hr(s), Charge: ₹${res.charge}`
      );
      setVehicleNumber("");
    } catch (err: any) {
      setMessage(err.response?.data?.detail || "Vehicle exit failed");
    }
  };

  return (
    <form className="card" onSubmit={handleExit}>
      <input
        type="text"
        placeholder="Vehicle Number"
        value={vehicleNumber}
        onChange={(e) => setVehicleNumber(e.target.value)}
        required
      />

      <button className="btn danger" type="submit">
        Exit Vehicle
      </button>

      {message && <p>{message}</p>}
    </form>
  );
}