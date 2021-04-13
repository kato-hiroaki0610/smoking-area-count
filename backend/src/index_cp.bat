@echo off
chcp 65001

@call cd web

@call cp index.html index_5階.html
@call cp index.html index_9階.html
@call cp index.html index_11階.html
@call cp index.html index_5階_9階.html
@call cp index.html index_5階_11階.html
@call cp index.html index_9階_11階.html

@call cp main.js 5階.js
@call cp main.js 9階.js
@call cp main.js 11階.js
@call cp main.js 5階_9階.js
@call cp main.js 5階_11階.js
@call cp main.js 9階_11階.js