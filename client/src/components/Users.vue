<template>
  <div class="container">
    <div class="jumbotron mt-5">
      <div class="col-sm-8 mx-auto">
        <h1 class="text-center">USERS</h1><br>
      </div>
      <table class="table col-md-10 mx-auto">
        <tbody>
          <ul>
            <li v-for="item in info">
              <tr>
                <td>Name:</td>
                <td> {{ item.name }} </td>
              </tr>
              <tr>
                <td>Last Active:</td>
                <td> {{ item.last_active }} </td>
                <td><router-link :to="'../users/' + item.id + '/'">Profile</router-link></td>
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
      .get('http://127.0.0.1:5000/users')
      .then(response => (this.info = response.data))
  }
}
</script>
