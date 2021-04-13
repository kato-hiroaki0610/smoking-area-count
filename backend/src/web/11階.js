(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! E:\project\smoking-area-count\frontend\src\main.ts */"zUnb");


/***/ }),

/***/ "AytR":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
const environment = {
    production: false
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "IX+F":
/*!*****************************!*\
  !*** ./src/config/api.json ***!
  \*****************************/
/*! exports provided: apiSetting, default */
/***/ (function(module) {

module.exports = JSON.parse("{\"apiSetting\":{\"api\":{\"/\":false,\"specified\":true,\"multiple\":false},\"room\":[\"11階\"]}}");

/***/ }),

/***/ "Sy1n":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _header_header_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./header/header.component */ "fECr");
/* harmony import */ var _card_card_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./card/card.component */ "mJ8H");



class AppComponent {
}
AppComponent.ɵfac = function AppComponent_Factory(t) { return new (t || AppComponent)(); };
AppComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: AppComponent, selectors: [["app-root"]], decls: 2, vars: 0, template: function AppComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "app-header");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "app-card");
    } }, directives: [_header_header_component__WEBPACK_IMPORTED_MODULE_1__["HeaderComponent"], _card_card_component__WEBPACK_IMPORTED_MODULE_2__["CardComponent"]], styles: ["[_nghost-%COMP%] {\n  font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\";\n  font-size: 14px;\n  color: #333;\n  box-sizing: border-box;\n  -webkit-font-smoothing: antialiased;\n  -moz-osx-font-smoothing: grayscale;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uXFwuLlxcYXBwLmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0VBQ0ksMEpBQUE7RUFDQSxlQUFBO0VBQ0EsV0FBQTtFQUNBLHNCQUFBO0VBQ0EsbUNBQUE7RUFDQSxrQ0FBQTtBQUNKIiwiZmlsZSI6ImFwcC5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIjpob3N0IHtcclxuICAgIGZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFwiU2Vnb2UgVUlcIiwgUm9ib3RvLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmLCBcIkFwcGxlIENvbG9yIEVtb2ppXCIsIFwiU2Vnb2UgVUkgRW1vamlcIiwgXCJTZWdvZSBVSSBTeW1ib2xcIjtcclxuICAgIGZvbnQtc2l6ZTogMTRweDtcclxuICAgIGNvbG9yOiAjMzMzO1xyXG4gICAgYm94LXNpemluZzogYm9yZGVyLWJveDtcclxuICAgIC13ZWJraXQtZm9udC1zbW9vdGhpbmc6IGFudGlhbGlhc2VkO1xyXG4gICAgLW1vei1vc3gtZm9udC1zbW9vdGhpbmc6IGdyYXlzY2FsZTtcclxufSJdfQ== */"] });


/***/ }),

/***/ "ZAI4":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "jhN1");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./app-routing.module */ "vY5A");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app.component */ "Sy1n");
/* harmony import */ var _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/platform-browser/animations */ "R1ws");
/* harmony import */ var _card_card_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./card/card.component */ "mJ8H");
/* harmony import */ var _header_header_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./header/header.component */ "fECr");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @angular/common/http */ "tk/3");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @angular/core */ "fXoL");








class AppModule {
}
AppModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_7__["ɵɵdefineNgModule"]({ type: AppModule, bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"]] });
AppModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_7__["ɵɵdefineInjector"]({ factory: function AppModule_Factory(t) { return new (t || AppModule)(); }, providers: [], imports: [[
            _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
            _app_routing_module__WEBPACK_IMPORTED_MODULE_1__["AppRoutingModule"],
            _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_3__["BrowserAnimationsModule"],
            _angular_common_http__WEBPACK_IMPORTED_MODULE_6__["HttpClientModule"]
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_7__["ɵɵsetNgModuleScope"](AppModule, { declarations: [_app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"],
        _card_card_component__WEBPACK_IMPORTED_MODULE_4__["CardComponent"],
        _header_header_component__WEBPACK_IMPORTED_MODULE_5__["HeaderComponent"]], imports: [_angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
        _app_routing_module__WEBPACK_IMPORTED_MODULE_1__["AppRoutingModule"],
        _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_3__["BrowserAnimationsModule"],
        _angular_common_http__WEBPACK_IMPORTED_MODULE_6__["HttpClientModule"]] }); })();


/***/ }),

/***/ "fECr":
/*!********************************************!*\
  !*** ./src/app/header/header.component.ts ***!
  \********************************************/
/*! exports provided: HeaderComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HeaderComponent", function() { return HeaderComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");

class HeaderComponent {
    constructor() {
        this.pageTitle = '喫煙室利用者数カウント';
    }
    get title() {
        return this.pageTitle;
    }
    ngOnInit() {
    }
}
HeaderComponent.ɵfac = function HeaderComponent_Factory(t) { return new (t || HeaderComponent)(); };
HeaderComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: HeaderComponent, selectors: [["app-header"]], decls: 4, vars: 1, consts: [["role", "banner", 1, "header"], ["id", "title"]], template: function HeaderComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "span");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.title);
    } }, styles: [".header[_ngcontent-%COMP%] {\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 80px;\n  display: flex;\n  align-items: center;\n  background-color: #2196f3;\n  color: white;\n  font-weight: 600;\n  border-bottom: solid 5px #64b5f6;\n}\n\ndiv#title[_ngcontent-%COMP%] {\n  font-size: 4vw;\n  margin-left: 10px;\n  flex: 1;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uXFwuLlxcLi5cXGhlYWRlci5jb21wb25lbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtFQUNJLGtCQUFBO0VBQ0EsTUFBQTtFQUNBLE9BQUE7RUFDQSxRQUFBO0VBQ0EsWUFBQTtFQUNBLGFBQUE7RUFDQSxtQkFBQTtFQUNBLHlCQUFBO0VBQ0EsWUFBQTtFQUNBLGdCQUFBO0VBQ0EsZ0NBQUE7QUFDSjs7QUFFQTtFQUNJLGNBQUE7RUFDQSxpQkFBQTtFQUNBLE9BQUE7QUFDSiIsImZpbGUiOiJoZWFkZXIuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyIuaGVhZGVyIHtcclxuICAgIHBvc2l0aW9uOiBhYnNvbHV0ZTtcclxuICAgIHRvcDogMDtcclxuICAgIGxlZnQ6IDA7XHJcbiAgICByaWdodDogMDtcclxuICAgIGhlaWdodDogODBweDtcclxuICAgIGRpc3BsYXk6IGZsZXg7XHJcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xyXG4gICAgYmFja2dyb3VuZC1jb2xvcjogIzIxOTZmMztcclxuICAgIGNvbG9yOiB3aGl0ZTtcclxuICAgIGZvbnQtd2VpZ2h0OiA2MDA7XHJcbiAgICBib3JkZXItYm90dG9tOiBzb2xpZCA1cHggIzY0YjVmNjtcclxufVxyXG5cclxuZGl2I3RpdGxlIHtcclxuICAgIGZvbnQtc2l6ZTogNHZ3O1xyXG4gICAgbWFyZ2luLWxlZnQ6IDEwcHg7XHJcbiAgICBmbGV4OiAxO1xyXG59Il19 */"] });


/***/ }),

/***/ "mJ8H":
/*!****************************************!*\
  !*** ./src/app/card/card.component.ts ***!
  \****************************************/
/*! exports provided: CardComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CardComponent", function() { return CardComponent; });
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! rxjs */ "qCKp");
/* harmony import */ var _config_api_json__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../config/api.json */ "IX+F");
var _config_api_json__WEBPACK_IMPORTED_MODULE_1___namespace = /*#__PURE__*/__webpack_require__.t(/*! ../../config/api.json */ "IX+F", 1);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _room_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../room.service */ "w0Mr");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/common */ "ofXK");






function CardComponent_ng_container_2_div_8_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
} if (rf & 2) {
    const room_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtextInterpolate1"]("", room_r1.use, "\u4EBA");
} }
function CardComponent_ng_container_2_div_9_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](1, "0\u4EBA");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
} }
function CardComponent_ng_container_2_div_14_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
} if (rf & 2) {
    const room_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtextInterpolate1"]("", room_r1.wait, "\u4EBA");
} }
function CardComponent_ng_container_2_div_15_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](1, "0\u4EBA");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
} }
function CardComponent_ng_container_2_div_20_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
} if (rf & 2) {
    const room_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtextInterpolate1"]("", room_r1.limit, "\u4EBA");
} }
function CardComponent_ng_container_2_div_21_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](1, "0\u4EBA");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
} }
function CardComponent_ng_container_2_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](1, "div", 3);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](2, "div", 4);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](3, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](5, "div", 5);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](6, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](7, "\u5229\u7528\u8005");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](8, CardComponent_ng_container_2_div_8_Template, 2, 1, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](9, CardComponent_ng_container_2_div_9_Template, 2, 0, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelement"](10, "div", 7);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](11, "div", 8);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](12, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](13, "\u5F85\u6A5F\u4E2D");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](14, CardComponent_ng_container_2_div_14_Template, 2, 1, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](15, CardComponent_ng_container_2_div_15_Template, 2, 0, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelement"](16, "div", 9);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](17, "div", 10);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](18, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtext"](19, "\u5B9A\u54E1\u4E0A\u9650");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](20, CardComponent_ng_container_2_div_20_Template, 2, 1, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](21, CardComponent_ng_container_2_div_21_Template, 2, 0, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const room_r1 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngClass", room_r1.is_limit ? "blinking" : "");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngClass", room_r1.is_limit ? "limit_color" : "unlimit_color");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtextInterpolate"](room_r1.room);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngIf", room_r1.use != "");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngIf", room_r1.use == "");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngIf", room_r1.wait != "");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngIf", room_r1.wait == "");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngIf", room_r1.limit != "");
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngIf", room_r1.limit == "");
} }
class CardComponent {
    constructor(roomService, router) {
        this.roomService = roomService;
        this.router = router;
        this.apis = ['', 'specified', 'multiple'];
        this.specifiedIndex = 1;
        this.rooms = ['5階', '9階', '11階'];
    }
    ngOnInit() {
        this.getRooms();
    }
    getAPI(currentAPI) {
        // valueがtrueのkeyのみ取得する
        // 戻り値は二重リスト
        // [[k, v]]
        const temp = Object.entries(currentAPI).filter(([k, v]) => v === true);
        const api = temp[0][0];
        const isExist = this.apis.includes(api);
        // APIがすべてFalseの場合または存在しないAPIの場合は '' となるようにする
        if (!api || !isExist) {
            return '';
        }
        // apiが複数Trueになっていても一つ目に格納されているものを返す
        return api;
    }
    getRoom(api, rooms) {
        // apiがspecifiedなのに部屋が複数指定されている場合、最初の一つを返す
        if (api === this.apis[this.specifiedIndex] && rooms.length > 1) {
            return rooms[0];
        }
        let result = '';
        const joinString = '&room=';
        rooms.forEach(r => {
            result += r + joinString;
        });
        // 末尾の'&room='を削除する
        return result.slice(0, -joinString.length);
    }
    getRooms() {
        const intervalTime = 2000;
        Object(rxjs__WEBPACK_IMPORTED_MODULE_0__["timer"])(0, intervalTime).subscribe(() => {
            const api = this.getAPI(_config_api_json__WEBPACK_IMPORTED_MODULE_1__["apiSetting"].api);
            const room = this.getRoom(api, _config_api_json__WEBPACK_IMPORTED_MODULE_1__["apiSetting"].room);
            this.roomService.getRooms(api, room)
                .subscribe((s) => {
                const roomsJson = s;
                // 文字列でアクセスしたら、Lintで警告されるが、
                // ピリオドでアクセスしたらエラーで動かないためTsLintの
                // no-string-literalをdisableにする
                // tslint:disable-next-line:no-string-literal
                this.roomStatus = roomsJson['room_status'];
            }, error => {
                console.error(error.status + ':' + error.statusText);
            });
        });
    }
}
CardComponent.ɵfac = function CardComponent_Factory(t) { return new (t || CardComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_room_service__WEBPACK_IMPORTED_MODULE_3__["RoomService"]), _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdirectiveInject"](_angular_router__WEBPACK_IMPORTED_MODULE_4__["Router"])); };
CardComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineComponent"]({ type: CardComponent, selectors: [["app-card"]], decls: 3, vars: 1, consts: [["role", "main", 1, "content"], [1, "card_wrapper"], [4, "ngFor", "ngForOf"], [1, "card", 3, "ngClass"], [1, "room_wrap", "room", "card_font", 3, "ngClass"], [1, "room_wrap", "room_use_wrap", "card_font"], [4, "ngIf"], [1, "room_spacer", "spacer_dashed"], [1, "room_wrap", "room_wait_wrap", "card_font"], [1, "room_spacer", "spacer_solid"], [1, "room_wrap", "room_limit_wrap", "card_font"]], template: function CardComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](0, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementStart"](1, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵtemplate"](2, CardComponent_ng_container_2_Template, 22, 9, "ng-container", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵproperty"]("ngForOf", ctx.roomStatus);
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_5__["NgForOf"], _angular_common__WEBPACK_IMPORTED_MODULE_5__["NgClass"], _angular_common__WEBPACK_IMPORTED_MODULE_5__["NgIf"]], styles: [".content[_ngcontent-%COMP%] {\n  height: calc(100% - 85px);\n  width: 100%;\n  position: relative;\n  top: 85px;\n  display: flex;\n  flex-direction: column;\n  overflow-y: scroll;\n  overflow-x: hidden;\n}\n\n.card_wrapper[_ngcontent-%COMP%] {\n  height: 100%;\n  width: 100%;\n}\n\n.card[_ngcontent-%COMP%] {\n  border-radius: 4px;\n  border: 1px solid #64b5f6;\n  color: white;\n  background-color: #2196f3;\n  height: 25vh;\n  width: 98vw;\n  margin: 5px 5px 5px 5px;\n  padding: 5px;\n  display: flex;\n  flex-direction: row;\n  justify-content: center;\n  align-items: center;\n  min-width: 30%;\n  position: relative;\n}\n\n.card_font[_ngcontent-%COMP%] {\n  font-size: 4vw;\n  font-weight: 800;\n  letter-spacing: 3px;\n}\n\n.room_wrap[_ngcontent-%COMP%] {\n  height: calc(25vh + (5px * 2) + (1px * 2));\n  display: flex;\n  flex-direction: column;\n  justify-content: center;\n  align-items: center;\n}\n\n.room_wrap[_ngcontent-%COMP%]   div[_ngcontent-%COMP%] {\n  height: 4vh;\n  padding: 2vw;\n}\n\n.room[_ngcontent-%COMP%] {\n  height: calc(25vh + (5px * 2));\n  width: 13vw;\n  max-width: 265px;\n  position: absolute;\n  left: -1px;\n  border-radius: 4px 0 0 4px;\n}\n\n.room_spacer[_ngcontent-%COMP%] {\n  height: calc(25vh + (5px * 2) + (1px * 2));\n  position: absolute;\n}\n\n.spacer_dashed[_ngcontent-%COMP%] {\n  border-right: dashed 6px #90caf9;\n  left: calc(13vw + 30vw);\n}\n\n.spacer_solid[_ngcontent-%COMP%] {\n  border-right: solid 6px #90caf9;\n  left: calc(13vw + 6px + 30vw + 30vw);\n}\n\n.room_use_wrap[_ngcontent-%COMP%] {\n  width: 30vw;\n  height: 5vh;\n  max-width: 700px;\n  position: absolute;\n  left: 13vw;\n}\n\n.room_wait_wrap[_ngcontent-%COMP%] {\n  width: 30vw;\n  max-width: 560px;\n  position: absolute;\n  left: calc(13vw + 30vw + 6px);\n}\n\n.room_limit_wrap[_ngcontent-%COMP%] {\n  width: 25vw;\n  max-width: 455px;\n  position: absolute;\n  right: 0;\n  top: 0;\n}\n\n.unlimit_color[_ngcontent-%COMP%] {\n  background-color: #00b020;\n}\n\n.limit_color[_ngcontent-%COMP%] {\n  background-color: #b00020;\n}\n\n.blinking[_ngcontent-%COMP%] {\n  animation: blink 1s ease-in-out infinite alternate;\n}\n\n@keyframes blink {\n  0% {\n    background: #2196f3;\n  }\n  100% {\n    background: #b00020;\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uXFwuLlxcLi5cXGNhcmQuY29tcG9uZW50LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBa0JBO0VBQ0kseUJBQUE7RUFDQSxXQUFBO0VBQ0Esa0JBQUE7RUFDQSxTQUFBO0VBQ0EsYUFBQTtFQUNBLHNCQUFBO0VBQ0Esa0JBQUE7RUFDQSxrQkFBQTtBQWpCSjs7QUFvQkE7RUFDSSxZQUFBO0VBQ0EsV0FBQTtBQWpCSjs7QUF3QkE7RUFDSSxrQkFBQTtFQUNBLHlCQUFBO0VBQ0EsWUFBQTtFQUNBLHlCQTVCUztFQTZCVCxZQTFDVTtFQTJDVixXQTVDUztFQTZDVCx1QkFBQTtFQUNBLFlBNUNrQjtFQTZDbEIsYUFBQTtFQUNBLG1CQUFBO0VBQ0EsdUJBQUE7RUFDQSxtQkFBQTtFQUNBLGNBQUE7RUFDQSxrQkFBQTtBQXJCSjs7QUF3QkE7RUFDSSxjQW5EYTtFQW9EYixnQkFBQTtFQUNBLG1CQUFBO0FBckJKOztBQXdCQTtFQUNJLDBDQW5EZTtFQW9EZixhQUFBO0VBQ0Esc0JBQUE7RUFDQSx1QkFBQTtFQUNBLG1CQUFBO0FBckJKOztBQXdCQTtFQUNJLFdBQUE7RUFDQSxZQUFBO0FBckJKOztBQXdCQTtFQUNJLDhCQUFBO0VBQ0EsV0F0RWtCO0VBdUVsQixnQkFBQTtFQUNBLGtCQUFBO0VBQ0EsVUFBQTtFQUNBLDBCQUFBO0FBckJKOztBQXdCQTtFQUNJLDBDQXpFZTtFQTBFZixrQkFBQTtBQXJCSjs7QUF3QkE7RUFDRSxnQ0FBQTtFQUNBLHVCQUFBO0FBckJGOztBQXdCQTtFQUNFLCtCQUFBO0VBQ0Esb0NBQUE7QUFyQkY7O0FBd0JBO0VBQ0ksV0E1RnNCO0VBNkZ0QixXQUFBO0VBQ0EsZ0JBQUE7RUFDQSxrQkFBQTtFQUNBLFVBakdrQjtBQTRFdEI7O0FBd0JBO0VBQ0ksV0FuR3VCO0VBb0d2QixnQkFBQTtFQUNBLGtCQUFBO0VBQ0EsNkJBQUE7QUFyQko7O0FBd0JBO0VBQ0ksV0F6R3dCO0VBMEd4QixnQkFBQTtFQUNBLGtCQUFBO0VBQ0EsUUFBQTtFQUNBLE1BQUE7QUFyQko7O0FBd0JBO0VBQ0kseUJBekdZO0FBb0ZoQjs7QUF3QkE7RUFDSSx5QkE5R1U7QUF5RmQ7O0FBd0JBO0VBR0ksa0RBQUE7QUFyQko7O0FBMENBO0VBQ0k7SUFDSSxtQkE3SUs7RUFzSFg7RUF5QkU7SUFDSSxtQkE5SU07RUF1SFo7QUFDRiIsImZpbGUiOiJjYXJkLmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiJGNhcmRfd2lkdGg6IDk4dnc7XHJcbiRjYXJkX2hlaWdodDogMjV2aDtcclxuJGNhcmRfcGFkZGluZ19oZWlnaHQ6IDVweDtcclxuJGNhcmRfbWFyZ2luX2hlaWdodDogMTBweDtcclxuJGNhcmRfYm9yZGVyX2hlaWdodDogMXB4O1xyXG4kY2FyZF9mb250X3NpemU6IDR2dztcclxuJHJvb21fY29udGVudHNfd2lkdGg6IDEzdnc7XHJcbiRyb29tX3VzZV9jb250ZW50c193aWR0aDogMzB2dztcclxuJHJvb21fd2FpdF9jb250ZW50c193aWR0aDogMzB2dztcclxuJHJvb21fbGltaXRfY29udGVudHNfd2lkdGg6IDI1dnc7XHJcbi8vIOWun+mam+OBq+eUu+mdouOBq+ihqOekuuOBleOCjOOCi+OCq+ODvOODieOBrumrmOOBlSBwYWRkaW5n44KEYm9yZGVy44Gu6auY44GV44KC5ZCr44KB44Gf5YCkXHJcbiRjYXJkX3ZpZXdfaGVpZ2h0OiBjYWxjKCN7JGNhcmRfaGVpZ2h0fSArICgjeyRjYXJkX3BhZGRpbmdfaGVpZ2h0fSAqIDIpICsgKCN7JGNhcmRfYm9yZGVyX2hlaWdodH0gKiAyKSk7XHJcbiRzcGFjZXJfY29sb3I6ICM5MGNhZjk7XHJcbiRzcGFjZXJfc2l6ZTogNnB4O1xyXG4kY2FyZF9jb2xvcjogIzIxOTZmMztcclxuJGNhcmRfYm9yZGVyX2NvbG9yOiAjNjRiNWY2O1xyXG4kbGltaXRfY29sb3I6ICNiMDAwMjA7XHJcbiR1bmxpbWl0X2NvbG9yOiAjMDBiMDIwO1xyXG4uY29udGVudCB7XHJcbiAgICBoZWlnaHQ6IGNhbGMoMTAwJSAtIDg1cHgpO1xyXG4gICAgd2lkdGg6IDEwMCU7XHJcbiAgICBwb3NpdGlvbjogcmVsYXRpdmU7XHJcbiAgICB0b3A6IDg1cHg7XHJcbiAgICBkaXNwbGF5OiBmbGV4O1xyXG4gICAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcclxuICAgIG92ZXJmbG93LXk6IHNjcm9sbDtcclxuICAgIG92ZXJmbG93LXg6IGhpZGRlbjtcclxufVxyXG5cclxuLmNhcmRfd3JhcHBlciB7XHJcbiAgICBoZWlnaHQ6IDEwMCU7XHJcbiAgICB3aWR0aDogMTAwJTtcclxuICAgIC8vIGRpc3BsYXk6IGZsZXg7XHJcbiAgICAvLyBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xyXG4gICAgLy8gYWxpZ24taXRlbXM6IGNlbnRlcjtcclxuICAgIC8vIGp1c3RpZnktY29udGVudDogY2VudGVyO1xyXG59XHJcblxyXG4uY2FyZCB7XHJcbiAgICBib3JkZXItcmFkaXVzOiA0cHg7XHJcbiAgICBib3JkZXI6IDFweCBzb2xpZCAkY2FyZF9ib3JkZXJfY29sb3I7XHJcbiAgICBjb2xvcjogd2hpdGU7XHJcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkY2FyZF9jb2xvcjtcclxuICAgIGhlaWdodDogJGNhcmRfaGVpZ2h0O1xyXG4gICAgd2lkdGg6ICRjYXJkX3dpZHRoO1xyXG4gICAgbWFyZ2luOiA1cHggNXB4IDVweCA1cHg7XHJcbiAgICBwYWRkaW5nOiAkY2FyZF9wYWRkaW5nX2hlaWdodDtcclxuICAgIGRpc3BsYXk6IGZsZXg7XHJcbiAgICBmbGV4LWRpcmVjdGlvbjogcm93O1xyXG4gICAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XHJcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xyXG4gICAgbWluLXdpZHRoOiAzMCU7XHJcbiAgICBwb3NpdGlvbjogcmVsYXRpdmU7XHJcbn1cclxuXHJcbi5jYXJkX2ZvbnQge1xyXG4gICAgZm9udC1zaXplOiAkY2FyZF9mb250X3NpemU7XHJcbiAgICBmb250LXdlaWdodDogODAwO1xyXG4gICAgbGV0dGVyLXNwYWNpbmc6IDNweDtcclxufVxyXG5cclxuLnJvb21fd3JhcCB7XHJcbiAgICBoZWlnaHQ6ICRjYXJkX3ZpZXdfaGVpZ2h0O1xyXG4gICAgZGlzcGxheTogZmxleDtcclxuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XHJcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcclxuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XHJcbn1cclxuXHJcbi5yb29tX3dyYXAgZGl2IHtcclxuICAgIGhlaWdodDogNHZoO1xyXG4gICAgcGFkZGluZzogMnZ3O1xyXG59XHJcblxyXG4ucm9vbSB7XHJcbiAgICBoZWlnaHQ6IGNhbGMoI3skY2FyZF9oZWlnaHR9ICsgKCN7JGNhcmRfcGFkZGluZ19oZWlnaHR9ICogMikpO1xyXG4gICAgd2lkdGg6ICRyb29tX2NvbnRlbnRzX3dpZHRoO1xyXG4gICAgbWF4LXdpZHRoOiAyNjVweDtcclxuICAgIHBvc2l0aW9uOiBhYnNvbHV0ZTtcclxuICAgIGxlZnQ6IC0xcHg7XHJcbiAgICBib3JkZXItcmFkaXVzOiA0cHggMCAwIDRweDtcclxufVxyXG5cclxuLnJvb21fc3BhY2VyIHtcclxuICAgIGhlaWdodDogJGNhcmRfdmlld19oZWlnaHQ7XHJcbiAgICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbn1cclxuXHJcbi5zcGFjZXJfZGFzaGVkIHtcclxuICBib3JkZXItcmlnaHQ6IGRhc2hlZCAkc3BhY2VyX3NpemUgJHNwYWNlcl9jb2xvcjtcclxuICBsZWZ0OiBjYWxjKCN7JHJvb21fY29udGVudHNfd2lkdGh9ICsgI3skcm9vbV91c2VfY29udGVudHNfd2lkdGh9KTtcclxufVxyXG5cclxuLnNwYWNlcl9zb2xpZCB7XHJcbiAgYm9yZGVyLXJpZ2h0OiBzb2xpZCAkc3BhY2VyX3NpemUgJHNwYWNlcl9jb2xvcjtcclxuICBsZWZ0OiBjYWxjKCN7JHJvb21fY29udGVudHNfd2lkdGh9ICsgI3skc3BhY2VyX3NpemV9ICsgI3skcm9vbV91c2VfY29udGVudHNfd2lkdGh9ICsgI3skcm9vbV93YWl0X2NvbnRlbnRzX3dpZHRofSk7XHJcbn1cclxuXHJcbi5yb29tX3VzZV93cmFwIHtcclxuICAgIHdpZHRoOiAkcm9vbV91c2VfY29udGVudHNfd2lkdGg7XHJcbiAgICBoZWlnaHQ6IDV2aDtcclxuICAgIG1heC13aWR0aDogNzAwcHg7XHJcbiAgICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbiAgICBsZWZ0OiAkcm9vbV9jb250ZW50c193aWR0aDtcclxufVxyXG5cclxuLnJvb21fd2FpdF93cmFwIHtcclxuICAgIHdpZHRoOiAkcm9vbV93YWl0X2NvbnRlbnRzX3dpZHRoO1xyXG4gICAgbWF4LXdpZHRoOiA1NjBweDtcclxuICAgIHBvc2l0aW9uOiBhYnNvbHV0ZTtcclxuICAgIGxlZnQ6IGNhbGMoI3skcm9vbV9jb250ZW50c193aWR0aH0gKyAjeyRyb29tX3VzZV9jb250ZW50c193aWR0aH0gKyAjeyRzcGFjZXJfc2l6ZX0pO1xyXG59XHJcblxyXG4ucm9vbV9saW1pdF93cmFwIHtcclxuICAgIHdpZHRoOiAkcm9vbV9saW1pdF9jb250ZW50c193aWR0aDtcclxuICAgIG1heC13aWR0aDogNDU1cHg7XHJcbiAgICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbiAgICByaWdodDogMDtcclxuICAgIHRvcDogMDtcclxufVxyXG5cclxuLnVubGltaXRfY29sb3Ige1xyXG4gICAgYmFja2dyb3VuZC1jb2xvcjogJHVubGltaXRfY29sb3I7XHJcbn1cclxuXHJcbi5saW1pdF9jb2xvciB7XHJcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkbGltaXRfY29sb3I7XHJcbn1cclxuXHJcbi5ibGlua2luZyB7XHJcbiAgICAtd2Via2l0LWFuaW1hdGlvbjogYmxpbmsgMXMgZWFzZS1pbi1vdXQgaW5maW5pdGUgYWx0ZXJuYXRlO1xyXG4gICAgLW1vei1hbmltYXRpb246IGJsaW5rIDFzIGVhc2UtaW4tb3V0IGluZmluaXRlIGFsdGVybmF0ZTtcclxuICAgIGFuaW1hdGlvbjogYmxpbmsgMXMgZWFzZS1pbi1vdXQgaW5maW5pdGUgYWx0ZXJuYXRlO1xyXG59XHJcblxyXG5ALXdlYmtpdC1rZXlmcmFtZXMgYmxpbmsge1xyXG4gICAgMCUge1xyXG4gICAgICAgIGJhY2tncm91bmQ6ICRjYXJkX2NvbG9yO1xyXG4gICAgfVxyXG4gICAgMTAwJSB7XHJcbiAgICAgICAgYmFja2dyb3VuZDogJGxpbWl0X2NvbG9yO1xyXG4gICAgfVxyXG59XHJcblxyXG5ALW1vei1rZXlmcmFtZXMgYmxpbmsge1xyXG4gICAgMCUge1xyXG4gICAgICAgIGJhY2tncm91bmQ6ICRjYXJkX2NvbG9yO1xyXG4gICAgfVxyXG4gICAgMTAwJSB7XHJcbiAgICAgICAgYmFja2dyb3VuZDogJGxpbWl0X2NvbG9yO1xyXG4gICAgfVxyXG59XHJcblxyXG5Aa2V5ZnJhbWVzIGJsaW5rIHtcclxuICAgIDAlIHtcclxuICAgICAgICBiYWNrZ3JvdW5kOiAkY2FyZF9jb2xvcjtcclxuICAgIH1cclxuICAgIDEwMCUge1xyXG4gICAgICAgIGJhY2tncm91bmQ6ICRsaW1pdF9jb2xvcjtcclxuICAgIH1cclxufVxyXG4iXX0= */"] });


/***/ }),

/***/ "vY5A":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./app.component */ "Sy1n");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");




const routes = [
    { path: '', component: _app_component__WEBPACK_IMPORTED_MODULE_1__["AppComponent"] },
    { path: 'web/specified', component: _app_component__WEBPACK_IMPORTED_MODULE_1__["AppComponent"] },
    { path: 'web/multiple', component: _app_component__WEBPACK_IMPORTED_MODULE_1__["AppComponent"] },
    { path: '**', redirectTo: '', pathMatch: 'full' }
];
class AppRoutingModule {
}
AppRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: AppRoutingModule });
AppRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ factory: function AppRoutingModule_Factory(t) { return new (t || AppRoutingModule)(); }, imports: [[_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forRoot(routes)], _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](AppRoutingModule, { imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]], exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] }); })();


/***/ }),

/***/ "w0Mr":
/*!*********************************!*\
  !*** ./src/app/room.service.ts ***!
  \*********************************/
/*! exports provided: RoomService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "RoomService", function() { return RoomService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "tk/3");


class RoomService {
    constructor(http) {
        this.http = http;
        // フロントエンドとバックエンドでポートが異なると、CORSエラーになる
        // それを回避するためフロントエンドのポート番号「4200」を指定し
        // Angular CLIのリバースプロキシを利用してバックエンドとの通信を実現する
        // private host = 'http://localhost:4200/app';
        // buildしてhtmlを配置するだけならば、localhostで問題ない
        this.host = 'http://localhost:8000';
        this.specifiedHost = this.host + '/specified?room=';
        this.multipleHost = this.host + '/multiple?room=';
    }
    getRooms(api, room) {
        return this.callAPI(this.createAPI(api, room));
    }
    createAPI(api, room) {
        if (api === '') {
            return this.host;
        }
        else if (api === 'specified') {
            return this.specifiedHost + room;
        }
        else if (api === 'multiple') {
            return this.multipleHost + room;
        }
        return this.host;
    }
    callAPI(api) {
        console.log(api);
        const rooms = this.http.get(api);
        return rooms;
    }
}
RoomService.ɵfac = function RoomService_Factory(t) { return new (t || RoomService)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵinject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClient"])); };
RoomService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: RoomService, factory: RoomService.ɵfac, providedIn: 'root' });


/***/ }),

/***/ "zUnb":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "jhN1");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "ZAI4");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "AytR");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["enableProdMode"])();
}
_angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["platformBrowser"]().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(err => console.error(err));


/***/ }),

/***/ "zn8P":
/*!******************************************************!*\
  !*** ./$$_lazy_route_resource lazy namespace object ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "zn8P";

/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map