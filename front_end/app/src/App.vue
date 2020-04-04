<template>
  <div id="app">
    <Header />
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="6" offset="3">
          <BuildingType /> 
        </b-col>
      </b-row>
      <b-row>
        <b-col sm="6" offset="3">
          <LoadingType /> 
        </b-col>
      </b-row>
    </b-container>


    
  </div>
</template>

<script>
import Header from './components/Header.vue'
import BuildingType from './components/BuildingType.vue'
import LoadingType from './components/LoadingType.vue'


export default {
  name: 'App',
  components: {
    Header,
    BuildingType,
    LoadingType
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
