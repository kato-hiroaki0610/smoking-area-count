import { Component, OnInit } from '@angular/core';
import { RoomService } from '../room.service';
import { Room, RoomStatus } from './room-info';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})

export class CardComponent implements OnInit {
  roomStatus: RoomStatus[];
  isLimit: boolean;

  constructor(private roomService: RoomService) { }

  ngOnInit(): void {
    this.getRooms();
  }

  getRooms(): void {
    this.roomService.getRooms()
        .subscribe(rooms => {
          const room: Room[] = rooms;
          // 文字列でアクセスしたら、エラーが表示される。
          // ピリオドでアクセスしたら動かないためtslintで
          // no-string-literalをdisableにする
          // tslint:disable-next-line:no-string-literal
          this.roomStatus = room['room_status'];
          console.log(this.roomStatus);
        },
        error => {
          console.error(error.status + ':' + error.statusText);
        });
  }
}
