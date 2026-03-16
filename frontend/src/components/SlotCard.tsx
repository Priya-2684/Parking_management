import type { Slot } from "../types/slot";

export default function SlotCard({ slot }: { slot: Slot }) {
  return (
    <div className="slot-card">
      <h4>{slot.slot_number}</h4>
      <p>Type: {slot.slot_type}</p>
      <p>Status: {slot.status}</p>
    </div>
  );
}