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

  constructor(private http: HttpClient) { }

  getRooms(): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(this.host);
    return rooms;
  }
}
