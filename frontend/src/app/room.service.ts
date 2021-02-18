import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Room } from './card/room-info';
import { Rooms } from './card/mock-card';

@Injectable({
  providedIn: 'root'
})
export class RoomService {

  constructor() { }

  getRooms(): Observable<Room[]> {
    const rooms = of(Rooms);
    return rooms;
  }
}
