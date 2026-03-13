import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import axiosInstance from "../../api/axiosInstance";
import { useAuth } from "../../hooks/useAuth";

export default function Register() {
  const { user } = useAuth();
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  if (user?.role?.toLowerCase() !== "admin") {
    return <Navigate to="/dashboard" replace />;
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axiosInstance.post("/users/create-staff", {
        username,
        email,
        password,
      });

      setMessage(response.data.message || "Staff created successfully");

      setUsername("");
      setEmail("");
      setPassword("");

      setTimeout(() => {
        navigate("/dashboard");
      }, 1200);
    } catch (err: any) {
      console.error("Create staff error:", err);
      console.error("Response data:", err?.response?.data);

      setMessage(
        err?.response?.data?.detail ||
        err?.response?.data?.message ||
        "Registration failed"
      );
    }
  };

  return (
    <div className="auth-container">
      <form className="card auth-card" onSubmit={handleSubmit}>
        <h2>Register Staff</h2>

        <input
          type="text"
          placeholder="Staff Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Staff Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Staff Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button className="btn" type="submit">
          Create Staff
        </button>

        {message && <p>{message}</p>}
      </form>
    </div>
  );
}