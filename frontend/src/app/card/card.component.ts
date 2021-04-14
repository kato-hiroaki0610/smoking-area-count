import { Component, OnInit } from '@angular/core';

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

  private readonly apis: string[] = ['', 'specified', 'multiple'];
  private readonly specifiedIndex: number = 1;

  constructor(private roomService: RoomService) { }

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

  getRoom(api: string, rooms: string[]): string {
    // apiがspecifiedなのに部屋が複数指定されている場合、最初の一つを返す
    if (api === this.apis[this.specifiedIndex] && rooms.length > 1) {
      return rooms[0];
    }

    let result = '';
    const joinString = '&room=';
    rooms.forEach(r => {
      result += r + joinString;
    });

    // 末尾の'&room='を削除する
    return result.slice(0, -joinString.length);
  }

  getRooms(): void {
    const intervalTime = 2000;
    timer(0, intervalTime).subscribe(() => {
      const api: string = this.getAPI(apiSetting.api);
      const room: string = this.getRoom(api, apiSetting.room);
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
