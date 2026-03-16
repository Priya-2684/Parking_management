import { useEffect, useState } from "react";
import { createSlotApi, getSlotsApi } from "../api/slotApi";
import SlotCard from "../components/SlotCard";
import DashboardLayout from "../layouts/DashboardLayout";
import type { Slot } from "../types/slot";

export default function SlotManagement() {
  const [slotNumber, setSlotNumber] = useState("");
  const [slotType, setSlotType] = useState("Bike");
  const [slots, setSlots] = useState<Slot[]>([]);
  const [bulkCount, setBulkCount] = useState("5");
  const [message, setMessage] = useState("");

  const loadSlots = async () => {
    const res = await getSlotsApi();
    setSlots(res);
  };

  useEffect(() => {
    loadSlots();
  }, []);

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      await createSlotApi({
        slot_number: slotNumber,
        slot_type: slotType,
      });
      setSlotNumber("");
      setSlotType("Bike");
      setMessage(`Slot ${slotNumber} created successfully!`);
      loadSlots();
    } catch (err: any) {
      setMessage(err.response?.data?.detail || "Failed to create slot");
    }
  };

  const handleBulkCreate = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const count = parseInt(bulkCount);
      const prefix = slotType === "Bike" ? "B" : "C";
      
      // Find the next available slot number
      const existingSlots = slots.filter(s => s.slot_type === slotType);
      const existingNumbers = existingSlots
        .map(s => parseInt(s.slot_number.slice(1)))
        .filter(n => !isNaN(n))
        .sort((a, b) => b - a);
      
      const startNumber = existingNumbers.length > 0 ? existingNumbers[0] + 1 : 1;
      const createdSlots = [];

      for (let i = 0; i < count; i++) {
        const slotNumber = `${prefix}${startNumber + i}`;
        try {
          await createSlotApi({
            slot_number: slotNumber,
            slot_type: slotType,
          });
          createdSlots.push(slotNumber);
        } catch (err) {
          // Skip if slot already exists
        }
      }

      setMessage(`Created ${createdSlots.length} new ${slotType} slots: ${createdSlots.join(", ")}`);
      loadSlots();
    } catch (err: any) {
      setMessage("Failed to create bulk slots");
    }
  };

  return (
    <DashboardLayout>
      <h2>Slot Management</h2>

      {message && <div className="card" style={{ marginBottom: "20px", padding: "10px", backgroundColor: "#e7f3ff", border: "1px solid #007bff" }}>{message}</div>}

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", marginBottom: "30px" }}>
        {/* Single Slot Creation */}
        <form className="card" onSubmit={handleCreate}>
          <h3>Create Single Slot</h3>
          <input
            type="text"
            placeholder="Slot Number (e.g., B21)"
            value={slotNumber}
            onChange={(e) => setSlotNumber(e.target.value)}
            required
          />

          <select value={slotType} onChange={(e) => setSlotType(e.target.value)}>
            <option value="Bike">Bike</option>
            <option value="Car">Car</option>
          </select>

          <button className="btn" type="submit">
            Create Slot
          </button>
        </form>

        {/* Bulk Slot Creation */}
        <form className="card" onSubmit={handleBulkCreate}>
          <h3>Create Multiple Slots</h3>
          <input
            type="number"
            placeholder="Number of slots"
            value={bulkCount}
            onChange={(e) => setBulkCount(e.target.value)}
            min="1"
            max="50"
            required
          />

          <select value={slotType} onChange={(e) => setSlotType(e.target.value)}>
            <option value="Bike">Bike</option>
            <option value="Car">Car</option>
          </select>

          <button className="btn" type="submit">
            Create {bulkCount} {slotType} Slots
          </button>
        </form>
      </div>

      <div style={{ marginBottom: "20px" }}>
        <h3>Current Slots: {slots.length} Total</h3>
        <div style={{ display: "flex", gap: "20px", fontSize: "14px" }}>
          <span>Bike: {slots.filter(s => s.slot_type === "Bike").length}</span>
          <span>Car: {slots.filter(s => s.slot_type === "Car").length}</span>
          <span>Available: {slots.filter(s => s.status === "Available").length}</span>
          <span>Occupied: {slots.filter(s => s.status === "Occupied").length}</span>
        </div>
      </div>

      <div className="slot-grid">
        {slots.map((slot) => (
          <SlotCard key={slot.id} slot={slot} />
        ))}
      </div>
    </DashboardLayout>
  );
}