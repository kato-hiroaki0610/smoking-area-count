import { Component, OnInit } from '@angular/core';
import { RoomService } from '../room.service';
import { Room } from './room-info';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})

export class CardComponent implements OnInit {
  rooms: Room[];

  constructor(private roomService: RoomService) { }

  ngOnInit(): void {
    this.getRooms();
  }

  getRooms(): void {
    this.roomService.getRooms()
        .subscribe(rooms => this.rooms = rooms);
  }

}
