import { useEffect, useState } from "react";
import { getPricingApi, savePricingApi } from "../../api/pricingApi";
import DashboardLayout from "../../layouts/DashboardLayout";
import type { Pricing } from "../../types/pricing";

export default function PricingManagement() {
  const [vehicleType, setVehicleType] = useState("Bike");
  const [pricePerHour, setPricePerHour] = useState("");
  const [pricingList, setPricingList] = useState<Pricing[]>([]);

  const loadPricing = async () => {
    const data = await getPricingApi();
    setPricingList(data);
  };

  useEffect(() => {
    loadPricing();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      await savePricingApi({
        vehicle_type: vehicleType,
        price_per_hour: Number(pricePerHour),
      });
      setPricePerHour("");
      loadPricing();
    } catch (err: any) {
      alert(err.response?.data?.detail || "Failed to save pricing");
    }
  };

  return (
    <DashboardLayout>
      <h2>Pricing Management</h2>

      <form className="card" onSubmit={handleSubmit}>
        <select value={vehicleType} onChange={(e) => setVehicleType(e.target.value)}>
          <option value="Bike">Bike</option>
          <option value="Car">Car</option>
        </select>

        <input
          type="number"
          placeholder="Price per hour"
          value={pricePerHour}
          onChange={(e) => setPricePerHour(e.target.value)}
          required
        />

        <button className="btn" type="submit">
          Save Pricing
        </button>
      </form>

      <div className="card">
        <h3>Current Pricing</h3>
        <ul>
          {pricingList.map((item) => (
            <li key={item.id}>
              {item.vehicle_type} - ₹{item.price_per_hour}/hour
            </li>
          ))}
        </ul>
      </div>
    </DashboardLayout>
  );
}