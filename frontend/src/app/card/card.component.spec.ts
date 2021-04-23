import { HttpClient, HttpHandler } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ActionSequence } from 'selenium-webdriver';

import { CardComponent } from './card.component';

describe('CardComponent', () => {
  let component: CardComponent;
  let fixture: ComponentFixture<CardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CardComponent ],
      providers: [ HttpClient, HttpHandler ]
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

  it('getAPI', () => {
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

  it('QueryParameterで指定された部屋ができること', () => {
    const api = ['', 'specified', 'specified', 'multiple'];
    const rooms = [
                    ['5f'],
                    ['7f'],
                    ['9f', '12f'],
                    ['5f', '9f', '12f'],
    ];

    const expected = ['5f', '7f', '9f', '5f&room=9f&room=12f'];

    expected.forEach((value, i) => {
      const actual = component.getRoom(api[i], rooms[i]);
      expect(actual).toEqual(value);
    });
  });

  xit('getRooms', () => {
    fixture.detectChanges();
  });
});
