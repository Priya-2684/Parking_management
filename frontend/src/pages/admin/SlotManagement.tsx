import { useEffect, useState } from "react";
import { createSlotApi, getSlotsApi } from "../../api/slotApi";
import SlotCard from "../../components/parking/SlotCard";
import DashboardLayout from "../../layouts/DashboardLayout";
import type { Slot } from "../../types/slot";

export default function SlotManagement() {
  const [slotNumber, setSlotNumber] = useState("");
  const [slotType, setSlotType] = useState("Bike");
  const [slots, setSlots] = useState<Slot[]>([]);

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
      loadSlots();
    } catch (err: any) {
      alert(err.response?.data?.detail || "Failed to create slot");
    }
  };

  return (
    <DashboardLayout>
      <h2>Slot Management</h2>

      <form className="card" onSubmit={handleCreate}>
        <input
          type="text"
          placeholder="Slot Number"
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

      <div className="slot-grid">
        {slots.map((slot) => (
          <SlotCard key={slot.id} slot={slot} />
        ))}
      </div>
    </DashboardLayout>
  );
}