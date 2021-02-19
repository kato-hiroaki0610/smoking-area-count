export interface Room {
  room_status: RoomStatus[];
}

export interface RoomStatus {
  階数: string;
  利用者数: number;
  上限超え: boolean;
  待ち人数: number;
}
