type Props = {
  title: string;
  value: string | number;
};

export default function DashboardCards({ title, value }: Props) {
  return (
    <div className="slot-card">
      <h4>{title}</h4>
      <p style={{ fontSize: "28px", fontWeight: "bold" }}>{value}</p>
    </div>
  );
}