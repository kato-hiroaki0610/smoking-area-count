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
  private specifiedHost = 'http://localhost:4200/app/specified?';
  private multipleHost = 'http://localhost:4200/app/multiple?';

  private state;

  constructor(private http: HttpClient) { }

  getRooms(currentPath: string): Observable<Room[]> {
    console.log(currentPath);

    // APIとqueryを分割する
    const query = currentPath.split('?');

    if (query[0] === '/') {
      return this.getAllRooms();
    } else if (query[0] === '/specified') {
      const parameter = query[1];
      return this.getSpecifiedRoom(parameter);
    } else if (query[0] === '/multiple') {

    } else {
      return this.getAllRooms();
    }

    console.log(query);
    const rooms = this.http.get<Room[]>(this.host);
    return rooms;
  }

  getAllRooms(): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(this.host);
    return rooms;
  }

  getSpecifiedRoom(query: string): Observable<Room[]> {
    const room = this.http.get<Room[]>(this.specifiedHost + query);
    return room;
  }

  getMultipleRoom(): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(this.multipleHost);
    return rooms;
  }
}
