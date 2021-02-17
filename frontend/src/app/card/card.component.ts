import { Component, OnInit } from '@angular/core';
import { Room } from './mock-card';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})

export class CardComponent implements OnInit {

  rooms: Room[] = [
    { room: '7階', use: '7', wait: '3', limit: '7' },
    { room: '9階', use: '3', wait: '0', limit: '10' },
    { room: '12階', use: '10', wait: '10', limit: '10' },
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
