from pydantic import BaseModel

class DashboardStats(BaseModel):
    total_slots: int
    occupied_slots: int
    available_slots: int
    today_entries: int
    today_exits: int
    active_vehicles: int