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
                <td> {{ index }} </td>
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
          <router-link :to="'../'  + 'bookings/add/09022019'">Add</router-link>
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
  mounted () {
    axios
      .get('http://127.0.0.1:5000/users/' + this.$route.params.id + '/bookings')
      .then(response => (this.info = response.data))
  },
  filters: {
    formatDate: function (value) {
      if (value) {
        return moment(String(value)).format('MM/DD/YYYY')
      }
    }
  }
}
</script>
