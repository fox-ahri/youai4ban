<template>
  <div class="auth">
      <input type="text" v-model="userinfo.number">
      <input type="text" v-model="userinfo.password">
      <button @click="login">登录</button>
  </div>
</template>

<script>
export default {
  name: 'auth',
  data () {
    return {
      userinfo: {
        number: '201617020405',
        password: '123456'
      }
    }
  },
  methods: {
    login () {
      this.axios.post('http://127.0.0.1:9000/login/', this.userinfo).then(res => {
        if (res.data.code === 200) {
          localStorage.setItem('token', res.data.data.token)
          this.$router.push({ name: 'Index' })
        } else {
          console.log(res.data.msg)
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
</style>