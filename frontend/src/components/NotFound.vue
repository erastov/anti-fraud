<style>
  #notfound{
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    background-color: #fff;
  }
</style>
<template>
  <v-container class="pt-5" fluid grid-list-md>
    <v-layout row wrap>
      <v-flex>
        <div id="notfound">
          <h1>404 Not Found</h1>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
