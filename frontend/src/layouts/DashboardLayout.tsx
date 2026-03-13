import Navbar from "../components/common/Navbar";
import Sidebar from "../components/common/Sidebar";

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