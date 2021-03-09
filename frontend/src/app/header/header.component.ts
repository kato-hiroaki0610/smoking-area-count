import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  private _title = '喫煙室利用者数カウント';
  public get title(): string {
    return this._title;
  }

  constructor() { }

  ngOnInit(): void {
  }

}
