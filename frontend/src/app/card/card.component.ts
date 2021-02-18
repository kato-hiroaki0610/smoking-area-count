import { Component, OnInit } from '@angular/core';
import { RoomService } from '../room.service';
import { Room } from './room-info';
import { Rooms } from './mock-card';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})

export class CardComponent implements OnInit {
  rooms: Room[];

  constructor() { }

  ngOnInit(): void {
    this.rooms = Rooms;
  }

}
