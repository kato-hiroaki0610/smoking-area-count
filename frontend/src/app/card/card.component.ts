import { AppComponent } from './../app.component';
import { Component, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';

import { filter } from 'rxjs/operators';
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
  private currentPath: string;

  constructor(private roomService: RoomService, private router: Router) { }

  ngOnInit(): void {
      this.getUrl();
      this.getRooms();
  }

  getUrl(): void {
    this.router.events.pipe(
      filter(f => f instanceof NavigationEnd)
    ).subscribe((s: any) => {
        this.currentPath = s.url;
    });
  }

  getRooms(): void {
    const intervalTime = 2000;
    timer(0, intervalTime).subscribe(() => {
      this.roomService.getRooms(this.currentPath)
      .subscribe((rooms: Room[]) => {
        const room: Room[] = rooms;
        // 文字列でアクセスしたら、Lintで警告されるが、
        // ピリオドでアクセスしたらエラーで動かないためTsLintの
        // no-string-literalをdisableにする
        // tslint:disable-next-line:no-string-literal
        this.roomStatus = room['room_status'];
      },
      error => {
        console.error(error.status + ':' + error.statusText);
      });
    });
  }
}
