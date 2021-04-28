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
  // private host = 'http://localhost:4200/app';
  // buildしてhtmlを配置するだけならば、localhostで問題ない
  private readonly host = 'http://localhost:8000';
  private readonly specifiedHost = this.host + '/specified';
  private readonly multipleHost = this.host + '/multiple';

  constructor(private http: HttpClient) { }

  getRooms(api: string, room: string): Observable<Room[]> {
    return this.callAPI(this.createAPI(api, room));
  }

  createAPI(api: string, room: string): string {
    if (api === '') {
      return this.host;
    } else if (api === 'specified') {
      return this.specifiedHost + room;
    } else if (api === 'multiple') {
      return this.multipleHost + room;
    }

    return this.host;
  }

  callAPI(api: string): Observable<Room[]> {
    console.log(api);
    const rooms = this.http.get<Room[]>(api);
    return rooms;
  }
}
