import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { timer } from 'rxjs';

import { RoomService } from '../room.service';
import { Room, RoomStatus } from './room-info';

import { apiSetting } from '../../config/api.json';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})

export class CardComponent implements OnInit {
  public roomStatus: RoomStatus[];

  private apis: string[] = ['', 'specified', 'multiple'];
  private readonly rooms: string[] = ['5階', '9階', '11階'];

  private readonly currentAPI: number = 0;
  private readonly currentRoom: number[] = [0, 1];

  constructor(private roomService: RoomService, private router: Router) { }

  ngOnInit(): void {
      this.getRooms();
  }

  getAPI(currentAPI: object): string {
    // valueがtrueのkeyのみ取得する
    // 戻り値は二重リスト
    // [[k, v]]
    const temp = Object.entries(currentAPI).filter(([k, v]) => v === true);
    const api = temp[0][0];

    const isExist = this.apis.includes(api);
    // APIがすべてFalseの場合または存在しないAPIの場合は '' となるようにする
    if (!api || !isExist) {
      return '';
    }

    // apiが複数Trueになっていても一つ目に格納されているものを返す
    return api;
  }

  getRoom(currentRoom): string {
    // TODO: エラーチェック、specifiedなのに部屋が複数あるとか......
    let room = '';
    this.currentRoom.forEach(r => {
      room += this.rooms[r] + '&';
    });

    return room.slice(0, -1);
  }

  getRooms(): void {
    const intervalTime = 2000;
    timer(0, intervalTime).subscribe(() => {
      const api: string = this.getAPI(apiSetting.api);
      const room: string = this.getRoom(apiSetting.room);
      this.roomService.getRooms(api, room)
      .subscribe((s: Room[]) => {
        const roomsJson: Room[] = s;
        // 文字列でアクセスしたら、Lintで警告されるが、
        // ピリオドでアクセスしたらエラーで動かないためTsLintの
        // no-string-literalをdisableにする
        // tslint:disable-next-line:no-string-literal
        this.roomStatus = roomsJson['room_status'];
      },
      error => {
        console.error(error.status + ':' + error.statusText);
      });
    });
  }
}
