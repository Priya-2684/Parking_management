import EntryForm from "../components/EntryForm";
import DashboardLayout from "../layouts/DashboardLayout";

export default function VehicleEntry() {
  return (
    <DashboardLayout>
      <h2>Vehicle Entry</h2>
      <EntryForm />
    </DashboardLayout>
  );
}