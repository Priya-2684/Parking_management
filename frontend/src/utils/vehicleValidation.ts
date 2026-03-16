// Indian Vehicle Number Validation
// Pattern: AB12CD3456 (2 letters, 2 digits, 2 letters, 4 digits)

export const validateIndianVehicleNumber = (vehicleNumber: string): { isValid: boolean; message: string } => {
  // Remove spaces and convert to uppercase
  const cleanNumber = vehicleNumber.replace(/\s/g, '').toUpperCase();
  
  // Regex pattern for Indian vehicle number: AB12CD3456
  const pattern = /^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$/;
  
  if (!cleanNumber) {
    return { isValid: false, message: "Vehicle number is required" };
  }
  
  if (!pattern.test(cleanNumber)) {
    return { 
      isValid: false, 
      message: "Invalid format. Use format: AB12CD3456 (e.g., MH12AB1234)" 
    };
  }
  
  return { isValid: true, message: "" };
};

// Format vehicle number as user types (auto-formatting)
export const formatVehicleNumber = (input: string): string => {
  // Remove spaces and convert to uppercase
  let clean = input.replace(/\s/g, '').toUpperCase();
  
  // Limit to 10 characters
  if (clean.length > 10) {
    clean = clean.substring(0, 10);
  }
  
  return clean;
};
