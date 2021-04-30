import { RoomService } from './../room.service';
import { HttpClient, HttpHandler } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';

import { CardComponent } from './card.component';
import { Room } from './room-info';

describe('CardComponent', () => {
  let component: CardComponent;
  let fixture: ComponentFixture<CardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CardComponent ],
      providers: [ HttpClient, HttpHandler, RoomService ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CardComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('getAPIメソッドで期待するAPIが取得できること', () => {
    const api = [
      {'/': true, specified: false, multiple: false},
      {'/': false, specified: true, multiple: false},
      {'/': false, specified: false, multiple: true},
      {'/': false, specified: false, multiple: false},
      {hoge: true},
    ];

    const expected = ['', 'specified', 'multiple', '', ''];

    expected.forEach((value, i) => {
      const actual = component.getAPI(api[i]);
      expect(actual).toEqual(value);
    });
  });

  it('getRoomメソッドを呼びQueryParameterで指定した部屋が取得できること', () => {
    const api = ['', '', 'specified', 'specified', 'multiple'];
    const rooms = [
                    [''],
                    ['5f'],
                    ['7f'],
                    ['9f', '12f'],
                    ['5f', '9f', '12f'],
    ];

    const expected = ['', '', '?room=7f', '?room=9f', '?room=5f&room=9f&room=12f'];

    expected.forEach((value, i) => {
      const actual = component.getRoom(api[i], rooms[i]);
      expect(actual).toEqual(value);
    });
  });

  // spyの使い方がうまくいかず......
  xit('getRooms', async (done: DoneFn) => {
    let httpClient: HttpClient;
    httpClient = TestBed.inject(HttpClient);
    const roomService = new RoomService(httpClient);
    const spy = spyOn(roomService, 'getRooms');
    expect(spy).toBe(roomService.getRooms);

    const expected: Room[] = [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
          { room: '9f', use: 9, limit: false, wait: 2 },
          { room: '12f', use: 2, limit: false, wait: 1 },
        ]}
    ];

    // spy.and.returnValue(of(expected));
    spy.and.callFake((api: string, room: string) => {
      return of(expected);
    });

    const cardComponent = new CardComponent(roomService);

    const result = cardComponent.roomStatus;
    done();
    console.log('result! :' + result);
  });
});
