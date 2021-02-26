import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Room } from './card/room-info';

@Injectable({
  providedIn: 'root'
})
export class RoomService {

  // フロントエンドとバックエンドでポートが異なると、CORSエラーになる
  // それを回避するためフロントエンドのポート番号「4200」を指定し
  // Angular CLIのリバースプロキシを利用してバックエンドとの通信を実現する
  private host = 'http://localhost:4200/app';
  private specifiedHost = 'http://localhost:4200/app/specified?room=';
  private multipleHost = 'http://localhost:4200/app/multiple?room=';

  private state;

  constructor(private http: HttpClient) { }

  getRooms(currentPath): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(this.host);
    return rooms;
  }

  getAllRooms(currentPath): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(this.host);
    return rooms;
  }

  getSpecifiedRoom(): Observable<Room[]> {
    const room = this.http.get<Room[]>(this.specifiedHost);
    return room;
  }

  getMultipleRoom(): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(this.multipleHost);
    return rooms;
  }
}
