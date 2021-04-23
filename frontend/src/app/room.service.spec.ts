import { HttpClient } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { Room } from './card/room-info';

import { RoomService } from './room.service';

describe('RoomService', () => {
  let service: RoomService;
  let httpClient: HttpClient;
  let httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule
      ],
      providers: [
      ]
    });
    service = TestBed.inject(RoomService);

    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('APIを含めたURLが正しく作成できること', () => {
    const expected: string[] = [
      'http://localhost:8000',
      'http://localhost:8000/specified?room=5f',
      'http://localhost:8000/multiple?room=5f&room=7f',
      'http://localhost:8000',
    ];
    const api: string[] = ['', 'specified', 'multiple', 'hoge'];
    const room: string[] = ['5f', '5f', '5f&room=7f', ''];

    expected.forEach((value, i) => {
      const actual = service.createAPI(api[i], room[i]);
      expect(actual).toEqual(value);
    });
  });

  it('callAPIメソッドからAPIが正しく呼べること', () => {
    const apis: string[] = [
      'http://localhost:8000',
      'http://localhost:8000/specified?room=5f',
      'http://localhost:8000/multiple?room=5f&room=9f',
    ];

    const expected: Room[][] = [
      [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
          { room: '9f', use: 9, limit: false, wait: 2 },
          { room: '12f', use: 2, limit: false, wait: 1 },
        ]}
      ],
      [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
        ]}
      ],
      [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
          { room: '9f', use: 9, limit: false, wait: 2 },
        ]}
      ],
    ];

    apis.forEach((value, i) => {
      service.callAPI(value).subscribe(actual => {
        // `req.flush` で実際の検証を行う
        expect(actual).toEqual(expected[i]);
        expect(actual).toBeTruthy();
      });

      const req = httpTestingController.expectOne(value);
      expect(req.request.method).toEqual('GET');

      // サーバーからの疑似的な応答
      // ここで指定した引数がactualに入る
      req.flush(expected[i]);

      // 未処理のリクエストがないかの確認
      httpTestingController.verify();
    });
  });

  it('getRoomsメソッドからAPIが正しく呼べていること', () => {
    const api: string[] = ['', 'specified', 'multiple', 'hoge'];
    const room: string[] = ['5f', '5f', '5f&room=9f', ''];
    const expected: Room[][] = [
      [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
          { room: '9f', use: 9, limit: false, wait: 2 },
          { room: '12f', use: 2, limit: false, wait: 1 },
        ]}
      ],
      [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
        ]}
      ],
      [
        { room_status: [
          { room: '5f', use: 5, limit: false, wait: 3 },
          { room: '9f', use: 9, limit: false, wait: 2 },
        ]}
      ],
    ];
    const url: string[] = [
      'http://localhost:8000',
      'http://localhost:8000/specified?room=5f',
      'http://localhost:8000/multiple?room=5f&room=9f',
      'http://localhost:8000'
    ];

    expected.forEach((value, i) => {
      service.getRooms(api[i], room[i]).subscribe(actual => {
        // `req.flush` で実際の検証を行う
        expect(actual).toEqual(expected[i]);
        expect(actual).toBeTruthy();
      });

      const req = httpTestingController.expectOne(url[i]);
      expect(req.request.method).toEqual('GET');

      // サーバーからの疑似的な応答
      // ここで指定した引数がactualに入る
      req.flush(value);

      // 未処理のリクエストがないかの確認
      httpTestingController.verify();
    });
  });
});
