<template>
  <div class="container">
    <div class="jumbotron mt-5">
      <div class="col-sm-8 mx-auto">
        <h1 class="text-center">USER INFO</h1><br>
      </div>
      <table class="table col-md-10 mx-auto">
        <tbody>
              <tr>
                <td>Name:</td>
                <td> {{ info.name }} </td>
              </tr>
              <tr>
                <td>Last Active:</td>
                <td> {{ info.last_active }} </td>
              </tr>
              <tr>
                <td>
                </td>
                <td>
                  <router-link :to="'../' + info.id + '/bookings/'">Bookings</router-link>
                </td>
              </tr>
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
      .get('http://127.0.0.1:5000/users/' + this.$route.params.id)
      .then(response => (this.info = response.data))
  }
}
</script>
