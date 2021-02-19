export interface Room {
  room_status: RoomStatus[];
}

export interface RoomStatus {
  room: string;
  use: number;
  limit: boolean;
  wait: number;
}
