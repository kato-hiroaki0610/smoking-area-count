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
  private specifiedHost = this.host + '/specified?';
  private multipleHost = this.host + '/multiple?';

  constructor(private http: HttpClient) { }

  getRooms(currentPath: string): Observable<Room[]> {
    console.log(currentPath);

    // APIとqueryを分割する
    const query = currentPath.split('?');
    let url: string;
    if (query[0] === '/') {
      url = this.host;
    } else if (query[0] === '/specified') {
      url = this.specifiedHost + query[1];
    } else if (query[0] === '/multiple') {
      url = this.multipleHost + query[1];
    } else {
      url = this.host;
    }

    return this.callAPI(url);
  }

  callAPI(url: string): Observable<Room[]> {
    const rooms = this.http.get<Room[]>(url);
    return rooms;
  }
}
