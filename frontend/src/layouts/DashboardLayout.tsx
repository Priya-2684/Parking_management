import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Navbar />
      <div className="layout">
        <Sidebar />
        <div className="content">{children}</div>
      </div>
    </>
  );
}