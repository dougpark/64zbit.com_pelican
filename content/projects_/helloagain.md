Title: Hello Again Phaser
Date: 2026-03-22
Slug: projects/hello/indexagain
Summary: A small Phaser.js based game demo in Pelican.
Status: published
Tags: phaser, game

Welcome Embeded Hello Phaser! A quick demo of embeding the full Phaser project into a blog post. Now with mouse tracking demo.

{% set base = "/projects/hello" %}

<div id="game-wrapper" style="position: relative; width: 100%; padding-top: 75%; /* 4:3 aspect ratio */">
  <div id="game-container" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
</div>

<script src="https://unpkg.com/phaser@3/dist/phaser.js"></script>

<script src="{{ base }}/main.js"></script>
