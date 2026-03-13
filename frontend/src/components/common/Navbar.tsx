import { useAuth } from "../../hooks/useAuth";
import { APP_NAME } from "../../utils/constants";

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <div className="navbar">
      <h2>{APP_NAME}</h2>
      <div>
        {user && (
          <span>
            {user.username} ({user.role})
          </span>
        )}
        <button className="btn danger" onClick={logout} style={{ marginLeft: "10px", width: "auto" }}>
          Logout
        </button>
      </div>
    </div>
  );
}