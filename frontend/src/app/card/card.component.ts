import { Component, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';

import { timer } from 'rxjs';

import { RoomService } from '../room.service';
import { Room, RoomStatus } from './room-info';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})

export class CardComponent implements OnInit {
  public roomStatus: RoomStatus[];

  // FIXME: いずれConfigファイルからよむような感じにしたい
  private readonly apis: string[] = ['', 'specified', 'multiple'];
  private readonly rooms: string[] = ['5階', '9階', '11階'];

  private readonly currentAPI: number = 0;
  private readonly currentRoom: number[] = [0, 1];

  constructor(private roomService: RoomService, private router: Router) { }

  ngOnInit(): void {
      this.getRooms();
  }

  getAPI(): string {
    const api: string = this.apis[this.currentAPI];
    return api;
  }

  getRoom(): string {
    let tempRoom = '';
    this.currentRoom.forEach(r => {
      tempRoom += this.rooms[r] + '&';
    });

    const room: string = tempRoom.slice(0, -1);
    return room;
  }

  getRooms(): void {
    const intervalTime = 2000;
    timer(0, intervalTime).subscribe(() => {
      const api: string = this.getAPI();
      const room: string = this.getRoom();
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
