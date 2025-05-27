Title: Hello Phaser
Date: 2025-05-25
Slug: projects/hello/index
Summary: A small JS-based game demo in Pelican.
Status: published
Tags: phaser, game

Welcome Embeded Hello Phaser!

{% set base = "/projects/hello" %}

<div id="game-wrapper" style="position: relative; width: 100%; padding-top: 75%; /* 4:3 aspect ratio */">
  <div id="game-container" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
</div>

<script src="https://unpkg.com/phaser@3/dist/phaser.js"></script>

<script src="{{ base }}/main.js"></script>
