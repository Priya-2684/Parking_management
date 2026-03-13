export const formatTime = (value: string | null) => {
  if (!value) return "-";
  return new Date(value).toLocaleString();
};