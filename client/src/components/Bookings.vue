<template>
  <div class="container">
    <div class="jumbotron mt-5">
      <div class="col-sm-8 mx-auto">
        <h1 class="text-center">BOOKINGS</h1><br>
      </div>
      <table class="table col-md-10 mx-auto">
        <tbody>
          <ul>
            <li v-for="(item, index) in info">
              <tr>
                <td>Date:</td>
                <td> {{ index|formatDate }} </td>
              </tr>
              <ul>
                <li v-for="value in item">
                  <tr>
                    <td>Title:</td>
                    <td> {{ value.title }} </td>
                  </tr>
                  <tr>
                    <td>Rating:</td>
                    <td> {{ value.rating }} </td>
                  </tr><br>
                </li>
              </ul>
            </li>
           </ul>
          <router-link v-if="check==true" :to="'../'  + 'bookings/add/09022019'">Add</router-link>
		  <router-link v-else to="/movies">Add</router-link>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  data () {
    return {
      info: null
    }
  },
  checker () {
    return {
      check: true,
	}
  },
  mounted () {
    axios
      .get('http://127.0.0.1:5000/users/' + this.$route.params.id + '/bookings')
      .then(response => (this.info = response.data))
    axios
	  .get('http://127.0.0.1:5000/showtimes')
	  .then( 
	    (response) => { this.check = true },
	    (error) => { this.check = false }
      );
  },
  filters: {
    formatDate: function (value) {
      if (value) {
        var symbols = value.split("")
        return (symbols[0] + symbols[1] + '/' + symbols[2] + symbols[3] + '/' + symbols[4] + symbols[5] + symbols[6] + symbols[7])
      }
    }
  }
}
</script>
