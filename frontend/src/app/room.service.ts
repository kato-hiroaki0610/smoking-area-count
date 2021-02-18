import { Injectable } from '@angular/core';
import { Room } from './card/room-info';
import { Rooms } from './card/mock-card';

@Injectable({
  providedIn: 'root'
})
export class RoomService {

  constructor() { }

  getRooms(): Room[] {
    return Rooms;
  }
}
