import type { ParkingRecord } from "../types/parking";
import { formatTime } from "../utils/formatTime";

export default function ParkingTable({ 
  data, 
  onQuickExit 
}: { 
  data: ParkingRecord[]; 
  onQuickExit?: (vehicleNumber: string, slotNumber: string) => void;
}) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Vehicle</th>
          <th>Type</th>
          <th>Slot</th>
          <th>Entry</th>
          <th>Exit</th>
          <th>Duration</th>
          <th>Charge</th>
          <th>Status</th>
          {onQuickExit && <th>Action</th>}
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td>{item.vehicle_number}</td>
            <td>{item.vehicle_type}</td>
            <td>{item.slot_number}</td>
            <td>{formatTime(item.entry_time)}</td>
            <td>{formatTime(item.exit_time)}</td>
            <td>{item.duration_hours ?? "-"}</td>
            <td>{item.charge ?? "-"}</td>
            <td>{item.status}</td>
            {onQuickExit && (
              <td>
                {item.status === "Active" && (
                  <button 
                    className="btn danger" 
                    style={{ padding: "5px 10px", fontSize: "12px" }}
                    onClick={() => onQuickExit(item.vehicle_number, item.slot_number)}
                  >
                    Exit
                  </button>
                )}
              </td>
            )}
          </tr>
        ))}
      </tbody>
    </table>
  );
}