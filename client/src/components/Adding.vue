<template>
  <div class="container">
    <div class="jumbotron mt-5">
      <div class="col-sm-8 mx-auto">
        <h1 class="text-center">FILMS (date: {{this.$route.params.date}}) </h1><br>
      </div>
      <table class="table col-md-10 mx-auto">
        <tbody>
              <ul>
                <li v-for="(value, index) in info">
                  <tr>
                    <td>Title:</td>	
                    <td> {{ value[0].title}} </td>
					<td> <button v-on:click="add(index)" type="button" class="btn btn-outline-dark">Book this</button> </td>
                  </tr>
                  <tr>
                    <td>Rating:</td>
                    <td> {{ value[0].rating }} </td>				
                  </tr><br>
                </li>
              </ul>
        </tbody>
		<tr>
		  <td>
		  <router-link :to="'../'  + 'add/' + prevpage">Previous Day</router-link>
		  </td>
		  <td>
		  <router-link :to="'../'  + 'add/' + nextpage" >Next Day</router-link>
		  </td>
		</tr>
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
  methods: {
    add: function (film_id, film_date) {
	  var film_date = this.$route.params.date	  
      
	  var film_id_arr = []
	  film_id_arr[0] = film_id
	  
	  var json = JSON.stringify({[film_date] : film_id_arr}) 
      let axiosConfig = {
      headers: {
          'Content-Type': 'application/json;charset=UTF-8',
          "Access-Control-Allow-Origin": "*"
      }
    };
	  
	  axios.post('http://127.0.0.1:5000/users/' + this.$route.params.id + '/bookings/add/' + film_date, json, axiosConfig)
    }
  },
  computed: {
    prevpage: function () {
      var newStr = this.$route.params.date[0] + this.$route.params.date[1]
      var newInt = parseInt(newStr, 10) - 1

      if (newInt < 10) {
        newStr = '0' + newInt + this.$route.params.date[2] + this.$route.params.date[3] + this.$route.params.date[4] + this.$route.params.date[5] + this.$route.params.date[6] + this.$route.params.date[7]
      } else {
        newStr = newInt + this.$route.params.date[2] + this.$route.params.date[3] + this.$route.params.date[4] + this.$route.params.date[5] + this.$route.params.date[6] + this.$route.params.date[7]
      }

      return newStr
    },
    nextpage: function () {
      var newStr = this.$route.params.date[0] + this.$route.params.date[1]
      var newInt = parseInt(newStr, 10) + 1

      if (newInt < 10) {
        newStr = '0' + newInt + this.$route.params.date[2] + this.$route.params.date[3] + this.$route.params.date[4] + this.$route.params.date[5] + this.$route.params.date[6] + this.$route.params.date[7]
      } else {
        newStr = newInt + this.$route.params.date[2] + this.$route.params.date[3] + this.$route.params.date[4] + this.$route.params.date[5] + this.$route.params.date[6] + this.$route.params.date[7]
      }

      return newStr
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:5000/users/' + this.$route.params.id + '/bookings/add/' + this.$route.params.date)
      .then(response => (this.info = response.data))
  }
}
</script>
