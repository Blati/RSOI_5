<template>
  <div class="container">
    <div class="jumbotron mt-5">
      <div class="col-sm-8 mx-auto">
        <h1 class="text-center">Sorry, showtime service is unavalible at the moment, but you can see our repertoire below</h1><br>
      </div>
      <table class="table col-md-10 mx-auto">
        <tbody>
              <ul>
                <li v-for="value in info">
                  <tr>
                    <td>Title:</td>	
                    <td> {{ value.title}} </td>
                  </tr>
                  <tr>
                    <td>Rating:</td>
                    <td> {{ value.rating }} </td>				
                  </tr>
				  <tr>
                    <td>Director:</td>
                    <td> {{ value.director }} </td>				
                  </tr><br>
                </li>
              </ul>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:5000/movies')
      .then(response => (this.info = response.data))
  }
}
</script>
